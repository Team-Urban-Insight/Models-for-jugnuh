# Generated by Django 3.0.7 on 2020-09-02 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0004_auto_20200902_1953'),
        ('orders', '0004_auto_20200902_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='provider',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='basic.Service_Provider'),
        ),
    ]