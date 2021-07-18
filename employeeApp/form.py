from django import forms
from employeeApp.models import *

class Regform(forms.ModelForm):
    class Meta:
        model = NewRegistration
        fields = ('fname','lname','city','dob','email','image')

class EmpRegForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('fname','lname','city','dob','email','username','password',
        'rem_leaves','position','team','current_project','image')