# Generated by Django 3.0.8 on 2020-11-13 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0010_auto_20201103_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='admin_receive_donation_error_emails',
            field=models.BooleanField(default=True),
        ),
    ]