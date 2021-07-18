from django.shortcuts import render, redirect
from employeeApp.models import *
from django.contrib import messages
from employeeApp.form import *
from django.http import HttpResponse
from EmployeeManagementSystem import settings
from django.core.mail import send_mail
from random import random, randrange
from django.core.serializers.json import DjangoJSONEncoder
from django.forms.models import model_to_dict
import json
# Create your views here.
def index(request):
    if request.session.get('id'):
        return render(request, 'dashboard.html')
    print(request.session.get('data'))
    return render(request, 'index.html')


def manageSession(request, emp):
    temp = dict()
    request.session['admin'] = True if emp.is_admin else False
    emp = model_to_dict(emp)
    for val in emp:
        if val == 'image':
            continue
        temp[val] = emp[val]
    # print(temp)
    jsonstr = json.dumps(temp,cls=DjangoJSONEncoder)
    request.session['data'] = json.loads(jsonstr)


def login(request):
    print(request.session.get('id'))
    if request.session.get('id') is not None:
        return redirect(index,permanent=True)
    if request.method == "POST":
        if request.POST.get("em_un") and request.POST.get("password"):
            em = request.POST.get("em_un")
            pw = request.POST.get("password")
            emp = None
            try:
                emp = Employee.objects.get(email=em)
            except:
                try:
                    emp = Employee.objects.get(username=em)
                except:
                    pass
            if emp is not None:
                if emp.password == pw:
                    request.session['id'] = emp.id
                    manageSession(request, emp)
                    # print(request.session.get('id'))
                    return redirect(index)
                else:
                    messages.error(request,"Incorrect password!")
                    return render(request, "login.html")
            else:
                messages.error(request,"Incorrect email or username!")
                return render(request, "login.html")
        else:
            messages.error(request,"All fields are required!")
            return render(request, "login.html")
    else:
        return render(request, "login.html")


def logout(request):
    request.session.clear()
    return redirect(index)


def insert(request):
    if request.session.get('id') is not None:
        messages.error(request,"Employees can not register again.")
        return redirect(index)
    def checkData(request):
        ans = True
        if not request.POST.get('fname'):
            print('no fname')
            ans = False
        if not request.POST.get('lname'):
            print('no lname')
            ans = False
        if not request.POST.get('city'):
            print('no city')
            ans = False
        if not request.POST.get('dob'):
            print('no dob')
            ans = False
        if not request.POST.get('email'):
            print('no email')
            ans = False
        if not request.POST.get('image'):
            print('no image')
            ans = False
        return ans
        
    if request.method=="POST":
        print(request.POST)
        try:
            print(Employee.objects.get(email=request.POST.get('email')).fname)
            messages.error(request, "Email registered with other account, try with another Email.")
            return redirect(insert)
        except:
            try:
                print(NewRegistration.objects.get(email=request.POST.get('email')).fname)
                messages.error(request, "Email registered with other account, try with another Email.")
                return redirect(insert)
            except:
                emp = Regform(request.POST, request.FILES)
                if emp.is_valid():
                    emp.save()
                    messages.success(request,"The record succesfully saved. Will be updated shortly.")
                    return redirect(index)
                else:
                    messages.error(request,"Invalid form")
                    print(emp)
    return render(request,"register.html")


def dashboard(request):
    return render(request, 'dashboard.html')


def viewApplicants(request):
    result = NewRegistration.objects.all()
    return render(request, 'view-applicants.html', {"applicants": result})


def viewEmployees(request):
    result = Employee.objects.all()
    return render(request, 'view-employees.html', {'employees': result})


def viewEmpDetails(request, id):
    emp = Employee.objects.get(id=id)
    return render(request, 'view-employee.html', {'employee': emp})


def leaves(request, id):
    emp = Employee.objects.get(id=id)
    leaveRequestList = LeaveRequest.objects.filter(empId=emp)
    return render(request, 'recent-leaves.html', {'leaves':leaveRequestList, 'employee':emp, 'leavesTaken': 24-emp.rem_leaves+emp.lop_leaves })


def addEmp(request, id=None):
    def checkData(request):
        ans = True
        if not request.POST.get('fname'):
            messages.error(request, 'No first Name')
            ans = False
        if not request.POST.get('lname'):
            messages.error(request, 'No Last Name')
            ans = False
        if not request.POST.get('email'):
            messages.error(request, 'no email')
            ans = False
        if not request.POST.get('dob'):
            messages.error(request, 'no Date of Birth')
            ans = False
        if not request.POST.get('username'):
            messages.error(request, 'no username')
            ans = False
        if not request.POST.get('password'):
            messages.error(request, 'no password')
            ans = False
        if not request.POST.get('city'):
            messages.error(request, 'no city')
            ans = False
        if not request.POST.get('leaves'):
            messages.error(request, 'no leaves')
            ans = False
        if not request.POST.get('position'):
            messages.error(request, 'no position')
            ans = False
        if not request.POST.get('team'):
            messages.error(request, 'no team')
            ans = False
        if not request.POST.get('project'):
            messages.error(request, 'no project')
            ans = False
        return ans
    chars = [i for i in range(65, 91)] + [i for i in range(48,58)] + [i for i in range(97, 123)]
    def generate(num):
        ans = ''
        for i in range(num):
            ans += chr(chars[randrange(0,62)])
        return ans

    emp = NewRegistration.objects.get(id=id)

    x = emp.dob
    username = str(emp.id) + chr(randrange(97, 123)) + emp.fname[:2].lower() + chr(randrange(97, 123)) + emp.lname[1:3].lower() + chr(randrange(65, 91))
    password = generate(randrange(8,12))
    if request.method == "POST":
        if checkData(request):
            emp = Employee()
            emp.fname = request.POST.get('fname')
            emp.lname = request.POST.get('lname')
            emp.email = request.POST.get('email')
            emp.dob = request.POST.get('dob')
            emp.city = request.POST.get('city')
            emp.username = request.POST.get('username')
            emp.password = request.POST.get('password')
            emp.position = request.POST.get('position')
            emp.rem_leaves = request.POST.get('leaves')
            emp.team = request.POST.get('team')
            emp.image = request.POST.get('image')
            emp.current_project = request.POST.get('project')
            emp.save()
            messages.success(request,"The record succesfully inserted.")
            msg = 'Hi ' + request.POST.get('fname') + ' ' + request.POST.get('lname') + \
                ', You have been selected to be a part of Polaris.\nPlease check below for your username and password. \
                you may later change the password by visiting your Dashboard. \n\n \
                Your Username: ' + request.POST.get('username') + '\n' + 'Your Password: ' + request.POST.get('password') + \
                '.\n\nYou will be informed of your position and role shortly. Welcome onboard.'
            res = send_mail('Polaris Careers', msg, settings.EMAIL_HOST_USER, [request.POST.get('email')])
            if res == 1:
                print('done')
            else:
                print('done, Mail not sent')
            return redirect(viewEmployees)
        print("post data incorrect")
    return render(request,"add-employee.html",{"employee":emp,'dob': x,"username":username,"password":password})


def update(request,id):
    emp = Employee.objects.get(id=id)
    form = EmpRegForm(request.POST,instance=emp)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request,"The record succesfully updated.")
            return redirect(viewEmpDetails,id=id)
        else:
            messages.error(request, "form invalid")
    return render(request,"edit.html",{"employee":emp})


def deleteEntry(request, id):
    applicant = None
    try:
        applicant = NewRegistration.objects.get(id=id)
    except:
        messages.error(request, 'Entry does not exist.')
        return redirect(viewApplicants)
    applicant.delete()
    messages.success(request, "Record deleted.")
    return redirect(viewApplicants)


def delete(request,id):
    emp = None
    try:
        emp = Employee.objects.get(id=id)
    except:
        messages.error(request, 'Employee does not exist.')
        return redirect(viewEmployees)
    emp.delete()
    messages.success(request, 'Employee Record deleted.')
    return redirect(viewEmployees)


def publishNotice(request):
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('body'):
            notice = Notice()
            notice.title = request.POST.get('title')
            notice.body = request.POST.get('body')
            notice.save()
            messages.success(request, 'Notice published Successfully.')
            return redirect(dashboard)
        messages.error(request, 'All fields required')
    return render(request, 'publish-notice.html')


def viewNotice(request):
    notices = Notice.objects.order_by('-id')
    if len(notices) > 10:
        notices = notices[:10]
    return render(request, 'view-notice.html', {'notices': notices})


def requestLeave(request):
    if request.method == 'POST':
        if request.POST.get('leaveType') and request.POST.get('startDate') and request.POST.get('endDate'):
            leave = LeaveRequest()
            leave.empId = Employee.objects.get(id=request.session.get('id'))
            leave.leaveType = request.POST.get('leaveType')
            leave.startDate = request.POST.get('startDate')
            leave.endDate = request.POST.get('endDate')
            leave.reason = request.POST.get('reason')
            leave.save()
            messages.success(request, "Leave Requested successfully.")
            return redirect(index)
        else:
            messages.error(request, "All fields Required")
    return render(request, 'request-leave.html')


def leaveRequests(request):
    requests = LeaveRequest.objects.filter(decision='Pending')
    return render(request,'leaveRequests.html',{'requests':requests})


def rejectLeave(request, id):
    lr = LeaveRequest.objects.get(id=id)
    lr.decision = "Rejected"
    lr.save()
    messages.success(request, "Request Rejected.")
    return redirect(leaveRequests)


def acceptLeave(request, id):
    lr = LeaveRequest.objects.get(id=id)
    emp = lr.empId
    print(emp.fname, emp.lname)
    if emp.rem_leaves > 0:
        emp.rem_leaves -= 1
    else:
        emp.lop_leaves += 1
    emp.save()
    lr.decision = "Approved"
    lr.save()
    messages.success(request, 'Leave Approved.')
    return redirect(leaveRequests)


def changePassword(request):
    if request.method == 'POST':
        if request.POST.get('oldpass') and request.POST.get('pass') and request.POST.get('cnfpass'):
            emp = Employee.objects.get(id=request.session.get('id'))
            if request.POST.get('pass') == request.POST.get('cnfpass'):
                if request.POST.get('oldpass') == emp.password:
                    emp.password = request.POST.get('pass')
                    messages.success(request,"password changed successfully.")
                    manageSession(request, emp)
                    emp.save()
                    return redirect('viewEmpDetails/' + str(request.session.get('id')))
                else:
                    messages.error(request,'Old Password incorrect.')
            else:
                messages.error(request, 'New Passwords do not match')
        else:
            messages.error(request, "all fields are required.")
    return render(request, 'changePassword.html')


