# Generated by Django 3.0.5 on 2020-04-14 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('site_settings', '0004_generalsettings_currency'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GeneralSettings',
            new_name='GlobalSettings',
        ),
        migrations.RemoveField(
            model_name='settings2c2p',
            name='currency_code',
        ),
    ]
