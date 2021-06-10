# Generated by Django 3.1.11 on 2021-05-31 15:15

from django.db import migrations
import i18nfield.fields
import newstream.fields


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0026_auto_20210531_0653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesettings',
            name='_2c2p_frontend_label',
            field=i18nfield.fields.I18nCharField(default='2C2P(Credit Card)', help_text='The Gateway name to be shown on the frontend website.', max_length=255),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='manual_frontend_label',
            field=i18nfield.fields.I18nCharField(default='Manual', help_text='The Gateway name to be shown on the frontend website for admin-added donations.', max_length=255),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='offline_frontend_label',
            field=i18nfield.fields.I18nCharField(default='Offline', help_text='The Gateway name to be shown on the frontend website for offline donations.', max_length=255),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='offline_instructions_text',
            field=newstream.fields.I18nRichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='offline_thankyou_text',
            field=newstream.fields.I18nRichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='paypal_frontend_label',
            field=i18nfield.fields.I18nCharField(default='PayPal', help_text='The Gateway name to be shown on public-facing website.', max_length=255),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='paypal_legacy_frontend_label',
            field=i18nfield.fields.I18nCharField(default='PayPal - Legacy', help_text='The Gateway name to be shown on public-facing website for old Paypal transactions.', max_length=255),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='signup_footer_text',
            field=newstream.fields.I18nRichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='stripe_frontend_label',
            field=i18nfield.fields.I18nCharField(default='Stripe', help_text='The Gateway name to be shown on the frontend website.', max_length=255),
        ),
    ]