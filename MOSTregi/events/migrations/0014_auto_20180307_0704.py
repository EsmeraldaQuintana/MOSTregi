# Generated by Django 2.0.2 on 2018-03-07 12:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_auto_20180306_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demo_form',
            name='date_request',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 14, 12, 4, 36, 538708, tzinfo=utc), verbose_name='booking date requested'),
        ),
    ]
