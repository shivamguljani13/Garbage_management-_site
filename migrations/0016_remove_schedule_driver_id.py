# Generated by Django 2.0 on 2018-03-13 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_schedule_noofhouses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='driver_id',
        ),
    ]
