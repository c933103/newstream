# Generated by Django 3.0.8 on 2020-09-24 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0016_remove_donationform_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationform',
            name='amount_type',
            field=models.CharField(choices=[('fixed', 'Fixed Amount'), ('stepped', 'Fixed Steps'), ('custom', 'Custom Amount'), ('stepped_custom', 'Fixed Steps with Custom Amount Option')], max_length=20),
        ),
    ]
