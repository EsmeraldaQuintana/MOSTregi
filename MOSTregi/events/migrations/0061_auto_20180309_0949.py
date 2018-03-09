# Generated by Django 2.0.2 on 2018-03-09 14:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import events.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0060_auto_20180309_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingrequest',
            name='time_request',
            field=models.TimeField(default=events.models.current_hour, verbose_name='time requested'),
        ),
        migrations.AlterField(
            model_name='demo_form',
            name='date_request',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 16, 14, 49, 38, 738967, tzinfo=utc), verbose_name='booking date requested'),
        ),
    ]
