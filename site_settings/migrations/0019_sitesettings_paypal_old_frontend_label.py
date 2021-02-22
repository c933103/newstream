# Generated by Django 3.0.8 on 2021-02-22 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0018_auto_20210222_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='paypal_old_frontend_label',
            field=models.CharField(default='PayPal - Old', help_text='The Gateway name to be shown on public-facing website for old Paypal transactions.', max_length=255),
        ),
    ]
