# Generated by Django 3.1.11 on 2021-05-21 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newstream_user', '0009_auto_20210411_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='language_preference',
            field=models.CharField(blank=True, choices=[('en', 'English'), ('zh-hant', 'Traditional Chinese'), ('ms', 'Malay'), ('id-id', 'Indonesian'), ('tl', 'Tagalog')], max_length=10),
        ),
    ]
