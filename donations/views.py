import re
import secrets
import json
from pprint import pprint
from django.conf import settings
from django.db import IntegrityError
from django.db.models import Q
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView
from django.utils.translation import gettext_lazy as _
from django.utils import translation
from django.views.decorators.csrf import csrf_exempt

from newstream.functions import getSiteSettings, printvars
from site_settings.models import PaymentGateway
from .models import *
from .forms import *
from .functions import *
from donations.payment_gateways import InitPaymentGateway, InitEditRecurringPaymentForm, getEditRecurringPaymentHtml
User = get_user_model()


def donate(request):
    if request.user.is_authenticated:
        # skip step 1 (personal info) and go to step 2 (donation details)
        return redirect('donations:donation-details')
    else:
        # show login or sign-up options page
        return render(request, 'donations/signin_method.html')


def donation_details(request):
    siteSettings = getSiteSettings(request)
    if not request.user.is_authenticated:
        return redirect('donations:donate')
    form_template = 'donations/donation_details_form.html'
    form_blueprint = siteSettings.donation_form
    if not form_blueprint:
        raise Exception('Donation Form not yet set.')
    if request.method == 'POST':
        form = DonationDetailsForm(
            request.POST, request=request, blueprint=form_blueprint, label_suffix='')
        if form.is_valid():
            # process meta data
            donation_metas = process_donation_meta(request)

            # process donation amount
            if 'donation_amount_custom' in form.cleaned_data and form.cleaned_data['donation_amount_custom'] and form.cleaned_data['donation_amount_custom'] > 0:
                donation_amount = form.cleaned_data['donation_amount_custom']
            else:
                donation_amount = form.cleaned_data['donation_amount']

            # create pending donation
            payment_gateway = PaymentGateway.objects.get(
                pk=form.cleaned_data['payment_gateway'])
            order_id = gen_order_id(gateway=payment_gateway)
            donation = Donation(
                order_number=order_id,
                user=request.user,
                form=form_blueprint,
                gateway=payment_gateway,
                is_recurring=True if form.cleaned_data['donation_frequency'] == 'monthly' else False,
                donation_amount=donation_amount,
                currency=form.cleaned_data['currency'],
                payment_status=STATUS_PENDING,
                metas=donation_metas,
            )

            try:
                donation.save()

                if 'first_time_registration' in request.session:
                    dpmeta = DonationPaymentMeta(
                        donation=donation, field_key='is_user_first_donation', field_value=request.session['first_time_registration'])
                    dpmeta.save()
            except Exception as e:
                # Should rarely happen, but in case some bugs or order id repeats itself
                print(str(e), flush=True)
                form.add_error(None, 'Server error, please retry.')
                return render(request, form_template, {'form': form, 'donation_details_fields': DONATION_DETAILS_FIELDS})

            # redirect to payment_gateway
            gatewayManager = InitPaymentGateway(
                request, donation=donation)
            return gatewayManager.redirect_to_gateway_url()
        else:
            pprint(form.errors)
    else:
        form = DonationDetailsForm(
            request=request, blueprint=form_blueprint, label_suffix='')

    # see: https://docs.djangoproject.com/en/3.0/ref/forms/api/#django.forms.Form.field_order
    if form_blueprint.isAmountSteppedCustom():
        form.order_fields(
            ['donation_amount', 'donation_amount_custom', 'donation_frequency', 'payment_gateway'])
    else:
        form.order_fields(
            ['donation_amount', 'donation_frequency', 'payment_gateway'])
    return render(request, form_template, {'form': form, 'donation_details_fields': DONATION_DETAILS_FIELDS})


def thank_you(request):
    if 'return-donation-id' in request.session:
        donation = Donation.objects.get(
            pk=request.session['return-donation-id'])
        # logs user in
        if donation.user:
            login(request, donation.user,
                  backend='django.contrib.auth.backends.ModelBackend')
        return render(request, 'donations/thankyou.html', {'isValid': True, 'isFirstTime': donation.is_user_first_donation, 'donation': donation})
    if 'return-error' in request.session:
        return render(request, 'donations/thankyou.html', {'isValid': False, 'error_message': request.session['return-error']})
    return render(request, 'donations/thankyou.html', {'isValid': False, 'error_message': _('No Payment Data is received.')})


def cancelled(request):
    if 'return-donation-id' in request.session:
        donation = Donation.objects.get(
            pk=request.session['return-donation-id'])
        donation.payment_status = STATUS_CANCELLED
        # No need to update recurring_status as no subscription object has been created yet
        donation.save()
        # logs user in
        if donation.user:
            login(request, donation.user,
                  backend='django.contrib.auth.backends.ModelBackend')
        return render(request, 'donations/cancelled.html', {'isValid': True, 'isFirstTime': donation.is_user_first_donation, 'donation': donation})
    if 'return-error' in request.session:
        return render(request, 'donations/cancelled.html', {'isValid': False, 'error_message': request.session['return-error']})
    return render(request, 'donations/cancelled.html', {'isValid': False, 'error_message': _('No Payment Data is received.')})


@login_required
@csrf_exempt
def cancel_recurring(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        if 'subscription_id' not in json_data:
            print("No subscription_id in JSON body", flush=True)
            return HttpResponse(status=400)
        subscription_id = int(json_data['subscription_id'])
        subscription = get_object_or_404(Subscription, id=subscription_id)
        gatewayManager = InitPaymentGateway(
            request, subscription=subscription)
        resultSet = gatewayManager.cancel_recurring_payment()
        if resultSet['status'] == 'success':
            return JsonResponse({'status': resultSet['status'], 'button-html': str(_('View all renewals')), 'recurring-status': str(_(STATUS_CANCELLED.capitalize())), 'button-href': reverse('donations:my-renewals', kwargs={'id': subscription_id})})
        else:
            return JsonResponse({'status': resultSet['status'], 'reason': resultSet['reason']})
    else:
        return HttpResponse(400)


@login_required
@csrf_exempt
def toggle_recurring(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        if 'subscription_id' not in json_data:
            print("No subscription_id in JSON body", flush=True)
            return HttpResponse(status=400)
        subscription_id = int(json_data['subscription_id'])
        subscription = get_object_or_404(Subscription, id=subscription_id)
        gatewayManager = InitPaymentGateway(
            request, subscription=subscription)
        resultSet = gatewayManager.toggle_recurring_payment()
        if resultSet['status'] == 'success':
            return JsonResponse({'status': resultSet['status'], 'button-html': resultSet['button-html'], 'recurring-status': str(_(resultSet['recurring-status'].capitalize())), 'success-message': resultSet['success-message']})
        else:
            return JsonResponse({'status': resultSet['status'], 'reason': resultSet['reason']})
    else:
        return HttpResponse(400)


@login_required
def edit_recurring(request, id):
    subscription = get_object_or_404(Subscription, id=id)
    # Form object is initialized according to the specific gateway and if request.method=='POST'
    form = InitEditRecurringPaymentForm(request, subscription)
    if request.method == 'POST':
        if form.is_valid():
            # use gatewayManager to process the data in form.cleaned_data as required
            gatewayManager = InitPaymentGateway(
                request, subscription=subscription)
            gatewayManager.update_recurring_payment(form.cleaned_data)

            return redirect('donations:edit-recurring', id=id)

    return render(request, getEditRecurringPaymentHtml(subscription), {'form': form, 'subscription': subscription})


@login_required
def my_onetime_donations(request):
    donations = Donation.objects.filter(
        user=request.user, is_recurring=False).order_by('-created_at')
    siteSettings = getSiteSettings(request)
    return render(request, 'donations/my_onetime_donations.html', {'donations': donations, 'siteSettings': siteSettings})


@login_required
def my_recurring_donations(request):
    subscriptions = Subscription.objects.filter(
        user=request.user).order_by('-created_at')
    siteSettings = getSiteSettings(request)
    return render(request, 'donations/my_recurring_donations.html', {'subscriptions': subscriptions, 'siteSettings': siteSettings})


@login_required
def my_renewals(request, id):
    subscription = get_object_or_404(Subscription, id=id)
    renewals = Donation.objects.filter(
        subscription=subscription).order_by('-created_at')
    siteSettings = getSiteSettings(request)
    return render(request, 'donations/my_renewals.html', {'subscription': subscription, 'renewals': renewals, 'siteSettings': siteSettings})
