# Generated by Django 2.0.2 on 2018-03-09 16:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0068_auto_20180309_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demo_form',
            name='date_request',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 16, 16, 0, 28, 553405, tzinfo=utc), verbose_name='booking date requested'),
        ),
    ]