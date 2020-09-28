import stripe
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.utils.translation import gettext_lazy as _
from django.views.decorators.csrf import csrf_exempt

from newstream.functions import getSiteSettings, uuid4_str, getFullReverseUrl, printvars
from donations.models import Donation
from donations.functions import gen_order_id
from donations.payment_gateways.setting_classes import getStripeSettings
from .functions import initStripeApiKey, formatDonationAmount
from .factory import Factory_Stripe


@csrf_exempt
def create_checkout_session(request):
    initStripeApiKey(request)
    stripeSettings = getStripeSettings(request)
    siteSettings = getSiteSettings(request)

    donation_id = request.session.get('donation_id', None)

    if donation_id:
        # get donation
        donation = get_object_or_404(Donation, id=donation_id)

        # init session_kwargs with common parameters
        session_kwargs = {
            'payment_method_types': ['card'],
            'metadata': {
                'donation_id': donation.id
            },
            'success_url': getFullReverseUrl(
                    request, 'donations:return-from-stripe')+'?stripe_session_id={CHECKOUT_SESSION_ID}',
            'cancel_url': getFullReverseUrl(
                    request, 'donations:cancel-from-stripe')+'?stripe_session_id={CHECKOUT_SESSION_ID}',
            'idempotency_key': uuid4_str()
        }

        # try to get existing stripe customer
        customers = stripe.Customer.list(email=donation.user.email, limit=1)
        if len(customers['data']) > 0:
            session_kwargs['customer'] = customers['data'][0]['id']
        else:
            session_kwargs['customer_email'] = donation.user.email

        # Product should have been created by admin manually at the dashboard
        # if no product exists, create one here(double safety net)
        # todo: make sure the product_id in site_settings has been set by some kind of configuration enforcement before site is launched
        product_list = stripe.Product.list(active=True)
        product = None
        if len(product_list['data']) == 0:
            # create new product here
            product = stripe.Product.create(name=str(_(
                "Newstream Default Product for Donation")), idempotency_key=uuid4_str())
            # Update product id in site_settings & stripe settings
            siteSettings.stripe_product_id = product.id
            siteSettings.save()
            stripeSettings.product_id = product.id
        else:
            # get the product, should aim at the product with the specific product id
            for prod in product_list['data']:
                if prod.id == stripeSettings.product_id:
                    product = prod
        if product == None:
            print('Cannot initialize/get the stripe product instance', flush=True)
            return HttpResponse(status=500)

        # ad-hoc price is used
        amount_str = formatDonationAmount(
            donation.donation_amount, donation.currency)
        adhoc_price = {
            'unit_amount_decimal': amount_str,
            'currency': donation.currency.lower(),
            'product': product.id
        }
        if donation.is_recurring:
            adhoc_price['recurring'] = {
                'interval': 'month',
                'interval_count': 1
            }
        session_kwargs['line_items'] = [{
            'price_data': adhoc_price,
            'quantity': 1,
        }]

        # set session mode
        session_mode = 'payment'
        if donation.is_recurring:
            session_mode = 'subscription'
        session_kwargs['mode'] = session_mode

        # set metadata
        if donation.is_recurring:
            session_kwargs['subscription_data'] = {
                'metadata': {
                    'donation_id': donation.id
                }
            }
        else:
            session_kwargs['payment_intent_data'] = {
                'metadata': {
                    'donation_id': donation.id
                }
            }

        try:
            session = stripe.checkout.Session.create(**session_kwargs)
        except Exception as e:
            print('Cannot create stripe checkout session: '+str(e), flush=True)
            return HttpResponse(status=500)

        return JsonResponse({'id': session.id})
    return HttpResponse(status=500)


@csrf_exempt
def verify_stripe_response(request):
    # Set up gateway manager object with its linking donation, session, etc...
    gatewayManager = Factory_Stripe.initGatewayByVerification(request)

    if gatewayManager:
        return gatewayManager.process_webhook_response()
    return HttpResponse(status=400)


@csrf_exempt
def return_from_stripe(request):
    gatewayManager = Factory_Stripe.initGatewayByReturn(request)
    if gatewayManager:
        request.session['return-donation-id'] = gatewayManager.donation.id
    else:
        request.session['return-error'] = str(_(
            "Results returned from gateway is invalid."))
    return redirect('donations:thank-you')


@csrf_exempt
def cancel_from_stripe(request):
    gatewayManager = Factory_Stripe.initGatewayByReturn(request)
    if gatewayManager:
        request.session['return-donation-id'] = gatewayManager.donation.id

        if gatewayManager.session:
            if gatewayManager.session.mode == 'payment':
                try:
                    stripe.PaymentIntent.cancel(
                        gatewayManager.session.payment_intent)
                except Exception as e:
                    request.session['return-error'] = str(e)
            # for subscription mode, payment_intent is not yet created, so no need to cancel
    else:
        request.session['return-error'] = str(_(
            "Results returned from gateway is invalid."))
    return redirect('donations:cancelled')
