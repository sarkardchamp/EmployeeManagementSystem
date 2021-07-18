from django.contrib import admin
from employeeApp.models import *
# Register your models here.
admin.site.register(Employee)
admin.site.register(NewRegistration)
admin.site.register(LeaveRequest)
admin.site.register(Notice)