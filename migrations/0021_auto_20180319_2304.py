# Generated by Django 2.0 on 2018-03-19 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0020_driver_info_driverarea'),
    ]

    operations = [
        migrations.DeleteModel(
            name='days',
        ),
        migrations.RenameField(
            model_name='driver_info',
            old_name='driverLicensePicture',
            new_name='driverLicPicture',
        ),
        migrations.RenameField(
            model_name='user_details',
            old_name='userDayDOB',
            new_name='notifications',
        ),
        migrations.RenameField(
            model_name='user_details',
            old_name='userMonthDOB',
            new_name='userDay',
        ),
        migrations.RenameField(
            model_name='user_details',
            old_name='userYearDOB',
            new_name='userMonth',
        ),
        migrations.AddField(
            model_name='garbagedetails',
            name='driver_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='garbagedetails',
            name='garbagePictureVerification',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schedule',
            name='driver_completion',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schedule',
            name='landmark',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='schedule',
            name='user_approval',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user_details',
            name='userYear',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='garbagedetails',
            name='garbagePicture',
            field=models.TextField(),
        ),
    ]
