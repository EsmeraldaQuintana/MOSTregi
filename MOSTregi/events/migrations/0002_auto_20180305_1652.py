# Generated by Django 2.0.2 on 2018-03-05 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='demo_form',
            old_name='date_time_recieved',
            new_name='date_time_received',
        ),
        migrations.RenameField(
            model_name='registration',
            old_name='date_time_recieved',
            new_name='date_time_received',
        ),
    ]
