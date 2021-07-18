from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Employee(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    dob = models.DateField()
    email = models.EmailField()
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=128)
    joining_date = models.DateField(editable=False, auto_now=True)
    city = models.CharField(max_length=70)
    rem_leaves = models.IntegerField(default=24)
    lop_leaves = models.IntegerField(default=0)
    is_admin = models.BooleanField(default=False)
    position = models.CharField(max_length=70, default='Entry Level')
    team = models.CharField(max_length=70, default='Not Allocated')
    current_project = models.CharField(max_length=128, default='Not Alotted')
    image = models.CharField(max_length=120)

    class Meta:
        db_table = "Employee"


class NewRegistration(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    dob = models.DateField()
    city = models.CharField(max_length=70)
    email = models.EmailField()
    image = models.ImageField(upload_to='images/reg')

    class Meta:
        db_table = "NewRegistration"


class LeaveRequest(models.Model):
    empId = models.ForeignKey(Employee,on_delete=CASCADE)
    leaveType = models.CharField(max_length=40)
    startDate = models.DateField()
    endDate = models.DateField()
    reason = models.TextField(max_length=300)
    decision = models.CharField(max_length=20,default="Pending")

    class Meta:
        db_table = "LeaveRequest"

class Notice(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    publish_date = models.DateField(editable=False,auto_now=True)