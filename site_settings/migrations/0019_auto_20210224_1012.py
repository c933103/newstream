# Generated by Django 3.0.8 on 2021-02-24 10:12

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0018_auto_20210222_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='offline_instructions_text',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='_2c2p_frontend_label',
            field=models.CharField(default='2C2P(Credit Card)', help_text='The Gateway name to be shown on the frontend website.', max_length=255),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='_2c2p_frontend_label_en',
            field=models.CharField(default='2C2P(Credit Card)', help_text='The Gateway name to be shown on the frontend website.', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='_2c2p_frontend_label_id_id',
            field=models.CharField(default='2C2P(Credit Card)', help_text='The Gateway name to be shown on the frontend website.', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='_2c2p_frontend_label_ms',
            field=models.CharField(default='2C2P(Credit Card)', help_text='The Gateway name to be shown on the frontend website.', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='_2c2p_frontend_label_tl',
            field=models.CharField(default='2C2P(Credit Card)', help_text='The Gateway name to be shown on the frontend website.', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='_2c2p_frontend_label_zh_hant',
            field=models.CharField(default='2C2P(Credit Card)', help_text='The Gateway name to be shown on the frontend website.', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='manual_frontend_label',
            field=models.CharField(default='Manual', help_text='The Gateway name to be shown on the frontend website for admin-added donations.', max_length=255),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='offline_frontend_label',
            field=models.CharField(default='Offline', help_text='The Gateway name to be shown on the frontend website for offline donations.', max_length=255),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='paypal_frontend_label',
            field=models.CharField(default='PayPal', help_text='The Gateway name to be shown on the frontend website.', max_length=255),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='paypal_frontend_label_en',
            field=models.CharField(default='PayPal', help_text='The Gateway name to be shown on the frontend website.', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='paypal_frontend_label_id_id',
            field=models.CharField(default='PayPal', help_text='The Gateway name to be shown on the frontend website.', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='paypal_frontend_label_ms',
            field=models.CharField(default='PayPal', help_text='The Gateway name to be shown on the frontend website.', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='paypal_frontend_label_tl',
            field=models.CharField(default='PayPal', help_text='The Gateway name to be shown on the frontend website.', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='paypal_frontend_label_zh_hant',
            field=models.CharField(default='PayPal', help_text='The Gateway name to be shown on the frontend website.', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='stripe_frontend_label',
            field=models.CharField(default='Stripe', help_text='The Gateway name to be shown on the frontend website.', max_length=255),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='stripe_frontend_label_en',
            field=models.CharField(default='Stripe', help_text='The Gateway name to be shown on the frontend website.', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='stripe_frontend_label_id_id',
            field=models.CharField(default='Stripe', help_text='The Gateway name to be shown on the frontend website.', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='stripe_frontend_label_ms',
            field=models.CharField(default='Stripe', help_text='The Gateway name to be shown on the frontend website.', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='stripe_frontend_label_tl',
            field=models.CharField(default='Stripe', help_text='The Gateway name to be shown on the frontend website.', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='stripe_frontend_label_zh_hant',
            field=models.CharField(default='Stripe', help_text='The Gateway name to be shown on the frontend website.', max_length=255, null=True),
        ),
    ]
