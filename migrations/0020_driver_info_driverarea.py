# Generated by Django 2.0 on 2018-03-18 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0019_user_details_isloggedin'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver_info',
            name='driverArea',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]