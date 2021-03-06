# Generated by Django 2.0.2 on 2018-03-09 13:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0051_auto_20180309_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingrequest',
            name='date_request',
            field=models.DateField(default=datetime.datetime(2018, 3, 9, 13, 58, 57, 206656, tzinfo=utc), verbose_name='date requested'),
        ),
        migrations.AlterField(
            model_name='demo_form',
            name='date_request',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 16, 13, 58, 57, 206060, tzinfo=utc), verbose_name='booking date requested'),
        ),
    ]
