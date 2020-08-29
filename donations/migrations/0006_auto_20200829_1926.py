# Generated by Django 3.0.8 on 2020-08-29 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0005_auto_20200821_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationform',
            name='fixed_amount',
            field=models.FloatField(blank=True, help_text='Define fixed donation amount if you chose "Fixed Amount" for your Amount Type. Decimal places should be no more than allowed for your current currency.', null=True),
        ),
    ]
