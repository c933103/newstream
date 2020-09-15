# Generated by Django 3.0.8 on 2020-09-15 19:44

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0013_auto_20200915_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amountstep',
            name='step',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=20),
        ),
        migrations.AlterField(
            model_name='donation',
            name='donation_amount',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
        migrations.AlterField(
            model_name='donationform',
            name='fixed_amount',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Define fixed donation amount if you chose "Fixed Amount" for your Amount Type. Decimal places should be no more than allowed for your current currency.', max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='recurring_amount',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
    ]
