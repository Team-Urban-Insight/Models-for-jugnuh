# Generated by Django 3.0.7 on 2020-09-02 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0003_auto_20200902_1854'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service_provider',
            name='phone_no',
        ),
        migrations.RemoveField(
            model_name='service_provider',
            name='rating',
        ),
        migrations.AddField(
            model_name='service_provider',
            name='avg_rating',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='service_provider',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='service_provider',
            name='police_verification_document',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='img/police_verification'),
        ),
        migrations.AddField(
            model_name='service_provider',
            name='profile_pic',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='img/profile_pics'),
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_no',
            field=models.BigIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='pincode',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='service_provider',
            name='aadhaar_card',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='img/aadhaar_image'),
        ),
        migrations.AlterField(
            model_name='service_provider',
            name='bank_account',
            field=models.CharField(blank=True, default=None, max_length=256, null=True),
        ),
    ]
