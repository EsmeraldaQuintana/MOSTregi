# Generated by Django 2.0.2 on 2018-03-06 13:05

from django.db import migrations
import django.utils.timezone
import events.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20180306_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='date_time_received',
            field=events.models.AutoDateTimeField(default=django.utils.timezone.now, verbose_name='booked on'),
        ),
    ]
