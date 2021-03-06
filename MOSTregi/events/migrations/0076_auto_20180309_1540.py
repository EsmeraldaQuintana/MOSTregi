# Generated by Django 2.0.2 on 2018-03-09 20:40

from django.db import migrations, models
import django.utils.timezone
import events.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0075_auto_20180309_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookingrequest',
            name='date_time_request',
        ),
        migrations.AddField(
            model_name='bookingrequest',
            name='date_request',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='date requested'),
        ),
        migrations.AddField(
            model_name='bookingrequest',
            name='time_request',
            field=models.TimeField(default=events.models.current_hour, verbose_name='time requested'),
        ),
    ]
