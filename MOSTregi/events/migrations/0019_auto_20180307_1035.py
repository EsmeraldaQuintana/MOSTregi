# Generated by Django 2.0.2 on 2018-03-07 15:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0018_auto_20180307_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demo_form',
            name='date_request',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 14, 15, 35, 39, 107421, tzinfo=utc), verbose_name='booking date requested'),
        ),
    ]