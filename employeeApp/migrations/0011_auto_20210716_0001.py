# Generated by Django 3.2.4 on 2021-07-15 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeApp', '0010_delete_leaverequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empId', models.IntegerField()),
                ('leaveType', models.CharField(max_length=40)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('reason', models.TextField(max_length=300)),
                ('decision', models.CharField(default='Pending', max_length=20)),
            ],
            options={
                'db_table': 'LeaveRequest',
            },
        ),
        migrations.AlterField(
            model_name='employee',
            name='current_project',
            field=models.CharField(default='Not Alotted', max_length=128),
        ),
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(default='Entry Level', max_length=70),
        ),
        migrations.AlterField(
            model_name='employee',
            name='team',
            field=models.CharField(default='Not Allocated', max_length=70),
        ),
    ]