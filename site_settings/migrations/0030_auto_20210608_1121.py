# Generated by Django 3.1.11 on 2021-06-08 11:21

from django.db import migrations
import functools
import i18nfield.fields
import newstream.utils


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0029_create_site_settings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesettings',
            name='_2c2p_frontend_label',
            field=i18nfield.fields.I18nCharField(default=functools.partial(newstream.utils.resolve_i18n_string, *('2C2P(Credit Card)',), **{}), help_text='The Gateway name to be shown on the frontend website.', max_length=255),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='manual_frontend_label',
            field=i18nfield.fields.I18nCharField(default=functools.partial(newstream.utils.resolve_i18n_string, *('Manual',), **{}), help_text='The Gateway name to be shown on the frontend website for admin-added donations.', max_length=255),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='offline_frontend_label',
            field=i18nfield.fields.I18nCharField(default=functools.partial(newstream.utils.resolve_i18n_string, *('Offline',), **{}), help_text='The Gateway name to be shown on the frontend website for offline donations.', max_length=255),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='paypal_frontend_label',
            field=i18nfield.fields.I18nCharField(default=functools.partial(newstream.utils.resolve_i18n_string, *('PayPal',), **{}), help_text='The Gateway name to be shown on public-facing website.', max_length=255),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='paypal_legacy_frontend_label',
            field=i18nfield.fields.I18nCharField(default=functools.partial(newstream.utils.resolve_i18n_string, *('PayPal - Legacy',), **{}), help_text='The Gateway name to be shown on public-facing website for old Paypal transactions.', max_length=255),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='stripe_frontend_label',
            field=i18nfield.fields.I18nCharField(default=functools.partial(newstream.utils.resolve_i18n_string, *('Stripe',), **{}), help_text='The Gateway name to be shown on the frontend website.', max_length=255),
        ),
    ]
