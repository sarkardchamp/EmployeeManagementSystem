from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('insert', views.insert, name='insert'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('addEmp/<int:id>', views.addEmp, name='addEmp'),
    path('update/<int:id>',views.update, name="update"),
    path('delete/<int:id>',views.delete, name="delete"),
    path('changePassword', views.changePassword, name='changePassword'),
    path('viewEmployees', views.viewEmployees, name='viewEmployees'),
    path('viewEmpDetails/<int:id>', views.viewEmpDetails, name='viewEmpDetails'),
    path('leaves/<int:id>', views.leaves, name='leaves'),
    path('viewApplicants', views.viewApplicants, name="viewApplicants"),
    path('deleteEntry/<int:id>', views.deleteEntry, name='deleteEntry'),
    path('publishNotice', views.publishNotice, name='publishNotice'),
    path('viewNotice', views.viewNotice, name='viewNotice'),
    path('acceptLeave/<int:id>', views.acceptLeave, name='acceptLeave'),
    path('rejectLeave/<int:id>', views.rejectLeave, name='rejectLeave'),
    path('leaveRequests', views.leaveRequests, name='leaveRequests'),
    path('requestLeave', views.requestLeave, name='requestLeave'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)