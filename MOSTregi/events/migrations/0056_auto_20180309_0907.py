# Generated by Django 2.0.2 on 2018-03-09 14:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0055_auto_20180309_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingrequest',
            name='date_request',
            field=models.DateField(default=datetime.datetime(2018, 3, 9, 14, 7, 32, 185815, tzinfo=utc), verbose_name='date requested'),
        ),
        migrations.AlterField(
            model_name='demo_form',
            name='date_request',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 16, 14, 7, 32, 185158, tzinfo=utc), verbose_name='booking date requested'),
        ),
    ]
