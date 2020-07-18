# Generated by Django 3.0.8 on 2020-07-18 08:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('email_campaigns', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='targetgroup',
            name='users',
            field=models.ManyToManyField(limit_choices_to={'is_email_verified': True, 'opt_in_mailing_list': True}, related_name='target_groups', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='campaign',
            name='recipients',
            field=models.ManyToManyField(to='email_campaigns.TargetGroup'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='template',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='email_campaigns.EmailTemplate'),
        ),
    ]
