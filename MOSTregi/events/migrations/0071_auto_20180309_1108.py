# Generated by Django 2.0.2 on 2018-03-09 16:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0070_auto_20180309_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demo_form',
            name='date_request',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 16, 16, 8, 45, 972124, tzinfo=utc), verbose_name='booking date requested'),
        ),
    ]
