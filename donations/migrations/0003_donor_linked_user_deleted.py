# Generated by Django 3.0.8 on 2020-07-19 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0002_auto_20200718_0834'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='linked_user_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
