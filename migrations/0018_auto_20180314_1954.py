# Generated by Django 2.0 on 2018-03-14 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0017_schedule_driver_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver_info',
            name='approved',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='user_details',
            name='device_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='driver_info',
            name='driverLicensePicture',
            field=models.ImageField(default='C://Users/varun/Desktop/Images/defaultpicture.png', upload_to='C://Users/varun/Desktop/Project/garbagemanagement/UserImages'),
        ),
        migrations.AlterField(
            model_name='garbagedetails',
            name='garbagePicture',
            field=models.ImageField(default='C://Users/varun/Desktop/Images/defaultpicture.png', upload_to='C://Users/varun/Desktop/Project/garbagemanagement/UserImages'),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='userProfilePicture',
            field=models.ImageField(default='C://Users/varun/Desktop/Images/defaultpicture.png', upload_to='C://Users/varun/Desktop/Project/garbagemanagement/UserImages'),
        ),
    ]
