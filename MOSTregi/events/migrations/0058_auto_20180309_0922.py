# Generated by Django 2.0.2 on 2018-03-09 14:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0057_auto_20180309_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingrequest',
            name='date_request',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='date requested'),
        ),
        migrations.AlterField(
            model_name='bookingrequest',
            name='time_request',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='time requested'),
        ),
        migrations.AlterField(
            model_name='demo_form',
            name='date_request',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 16, 14, 22, 54, 294483, tzinfo=utc), verbose_name='booking date requested'),
        ),
    ]
