# Generated by Django 2.0.2 on 2018-03-06 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20180305_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demo_form',
            name='date_time_received',
            field=models.DateTimeField(verbose_name='booked on'),
        ),
    ]
