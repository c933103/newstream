# Generated by Django 3.0.14 on 2021-04-27 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0029_auto_20210331_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='amountstep',
            name='default',
            field=models.BooleanField(default=False),
        ),
    ]
