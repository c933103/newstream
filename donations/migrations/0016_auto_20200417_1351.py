# Generated by Django 3.0.5 on 2020-04-17 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0015_donor_linked_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
