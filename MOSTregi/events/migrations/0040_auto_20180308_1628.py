# Generated by Django 2.0.2 on 2018-03-08 21:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0039_auto_20180308_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demo_form',
            name='date_request',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 15, 21, 28, 6, 962433, tzinfo=utc), verbose_name='booking date requested'),
        ),
    ]
