# Generated by Django 3.0.8 on 2021-02-24 10:37

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0019_auto_20210224_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='offline_thankyou_text',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]
