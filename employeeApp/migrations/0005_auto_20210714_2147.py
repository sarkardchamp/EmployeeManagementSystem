# Generated by Django 3.2.4 on 2021-07-14 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeApp', '0004_auto_20210708_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/employees'),
        ),
        migrations.AddField(
            model_name='newregistration',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/reg'),
        ),
    ]