# Generated by Django 2.0.2 on 2018-03-06 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20180306_0805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='date_request',
            field=models.DateField(verbose_name='date requested'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='time_request',
            field=models.TimeField(verbose_name='time requested'),
        ),
    ]