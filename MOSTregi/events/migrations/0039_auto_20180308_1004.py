# Generated by Django 2.0.2 on 2018-03-08 15:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0038_auto_20180307_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demo_form',
            name='date_request',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 15, 15, 4, 16, 155169, tzinfo=utc), verbose_name='booking date requested'),
        ),
    ]