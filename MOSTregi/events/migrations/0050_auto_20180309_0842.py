# Generated by Django 2.0.2 on 2018-03-09 13:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0049_auto_20180309_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demo_form',
            name='date_request',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 16, 13, 42, 23, 141270, tzinfo=utc), verbose_name='booking date requested'),
        ),
    ]
