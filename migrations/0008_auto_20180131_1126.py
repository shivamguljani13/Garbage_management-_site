# Generated by Django 2.0 on 2018-01-31 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_auto_20180127_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver_info',
            name='driverLicensePicture',
            field=models.ImageField(default='C://Users/varun/Desktop/Images/defaultpicture.png', upload_to='C://Users/varun/Desktop/Project/garbagemanagement/UserImages'),
        ),
        migrations.AlterField(
            model_name='driver_info',
            name='driverProfilePicture',
            field=models.ImageField(default='C://Users/varun/Desktop/Images/defaultpicture.png', upload_to='C://Users/varun/Desktop/Project/garbagemanagement/UserImages'),
        ),
    ]
