# Generated by Django 3.2.4 on 2021-07-17 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeApp', '0013_notice'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='publish_date',
            field=models.DateField(auto_now=True),
        ),
    ]
