# Generated by Django 3.1.11 on 2021-06-01 07:12

from django.db import migrations, models
import django.db.models.deletion
import i18nfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0027_auto_20210531_1515'),
    ]

    operations = [
        migrations.CreateModel(
            name='I18nAbstractFormField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('clean_name', models.CharField(blank=True, default='', help_text='Safe name of the form field, the label converted to ascii_snake_case', max_length=255, verbose_name='name')),
                ('field_type', models.CharField(choices=[('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('email', 'Email'), ('number', 'Number'), ('url', 'URL'), ('checkbox', 'Checkbox'), ('checkboxes', 'Checkboxes'), ('dropdown', 'Drop down'), ('multiselect', 'Multiple select'), ('radio', 'Radio buttons'), ('date', 'Date'), ('datetime', 'Date/time'), ('hidden', 'Hidden field')], max_length=16, verbose_name='field type')),
                ('required', models.BooleanField(default=True, verbose_name='required')),
                ('choices', models.TextField(blank=True, help_text='Comma separated list of choices. Only applicable in checkboxes, radio and dropdown.', verbose_name='choices')),
                ('default_value', models.CharField(blank=True, help_text='Default value. Comma separated values supported for checkboxes.', max_length=255, verbose_name='default value')),
                ('label', i18nfield.fields.I18nCharField(help_text='The label of the form field', max_length=255, verbose_name='label')),
                ('help_text', i18nfield.fields.I18nCharField(blank=True, max_length=255, verbose_name='help text')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='usermetafield',
            name='choices',
        ),
        migrations.RemoveField(
            model_name='usermetafield',
            name='clean_name',
        ),
        migrations.RemoveField(
            model_name='usermetafield',
            name='default_value',
        ),
        migrations.RemoveField(
            model_name='usermetafield',
            name='field_type',
        ),
        migrations.RemoveField(
            model_name='usermetafield',
            name='help_text',
        ),
        migrations.RemoveField(
            model_name='usermetafield',
            name='id',
        ),
        migrations.RemoveField(
            model_name='usermetafield',
            name='label',
        ),
        migrations.RemoveField(
            model_name='usermetafield',
            name='required',
        ),
        migrations.RemoveField(
            model_name='usermetafield',
            name='sort_order',
        ),
        migrations.AddField(
            model_name='usermetafield',
            name='i18nabstractformfield_ptr',
            field=models.OneToOneField(auto_created=True, default=None, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='site_settings.i18nabstractformfield'),
            preserve_default=False,
        ),
    ]
