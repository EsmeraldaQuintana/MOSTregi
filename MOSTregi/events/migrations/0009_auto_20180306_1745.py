# Generated by Django 2.0.2 on 2018-03-06 22:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20180306_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demo_form',
            name='date_request',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 13, 22, 45, 32, 648374, tzinfo=utc), verbose_name='booking date requested'),
        ),
    ]
