# Generated by Django 2.0 on 2018-01-27 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_driver_info_driverlicensepicture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver_info',
            name='driverLicensePicture',
            field=models.ImageField(default='C://Users/varun/Desktop/Images/defaultpicture.png', upload_to='C://Users/varun/Desktop/Project/garbagemanagement/LicenseImages'),
        ),
        migrations.AlterField(
            model_name='driver_info',
            name='driverProfilePicture',
            field=models.ImageField(default='C://Users/varun/Desktop/Images/defaultpicture.png', upload_to='C://Users/varun/Desktop/Project/garbagemanagement/DriverImages'),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='userProfilePicture',
            field=models.ImageField(default='C://Users/varun/Desktop/Images/defaultpicture.png', upload_to='C://Users/varun/Desktop/Project/garbagemanagement/UserImages'),
        ),
    ]
