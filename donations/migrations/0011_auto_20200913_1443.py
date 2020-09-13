# Generated by Django 3.0.8 on 2020-09-13 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('site_settings', '0004_sitesettings_stripe_product_id'),
        ('donations', '0010_remove_donation_is_user_first_donation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='recurring_status',
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.CharField(max_length=255)),
                ('recurring_amount', models.FloatField()),
                ('currency', models.CharField(max_length=20)),
                ('recurring_status', models.CharField(blank=True, choices=[('active', 'Active'), ('processing', 'Processing'), ('paused', 'Paused'), ('cancelled', 'Cancelled')], max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('linked_user_deleted', models.BooleanField(default=False)),
                ('deleted', models.BooleanField(default=False)),
                ('gateway', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='site_settings.PaymentGateway')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Subscription',
                'verbose_name_plural': 'Subscriptions',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='donation',
            name='subscription',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='donations.Subscription'),
        ),
    ]
