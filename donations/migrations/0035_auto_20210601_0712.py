# Generated by Django 3.1.11 on 2021-06-01 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0028_auto_20210601_0712'),
        ('donations', '0034_auto_20210601_0506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationmetafield',
            name='i18nabstractformfield_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='site_settings.i18nabstractformfield'),
        ),
        migrations.DeleteModel(
            name='I18nAbstractFormField',
        ),
    ]
