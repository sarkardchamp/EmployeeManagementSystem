# Generated by Django 3.2.4 on 2021-07-17 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeApp', '0015_employee_lop_leaves'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
