# Generated by Django 3.0.8 on 2020-12-19 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newstream_user', '0002_usersubscriptionupdateslog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersubscriptionupdateslog',
            name='action_type',
            field=models.CharField(choices=[('update-subscription', 'update-subscription'), ('pause-subscription', 'pause-subscription'), ('resume-subscription', 'resume-subscription')], max_length=255, null=True),
        ),
    ]