# Generated by Django 2.0.2 on 2018-03-09 11:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0040_auto_20180308_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demo_form',
            name='date_request',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 16, 11, 20, 42, 634548, tzinfo=utc), verbose_name='booking date requested'),
        ),
    ]
