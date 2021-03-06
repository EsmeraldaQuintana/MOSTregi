# Generated by Django 2.0.2 on 2018-03-08 02:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0037_auto_20180307_2126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demo_form',
            name='telephone',
        ),
        migrations.AlterField(
            model_name='demo_form',
            name='date_request',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 15, 2, 28, 38, 172631, tzinfo=utc), verbose_name='booking date requested'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='telephone',
            field=phonenumber_field.modelfields.PhoneNumberField(default='11111111111', max_length=128),
        ),
    ]
