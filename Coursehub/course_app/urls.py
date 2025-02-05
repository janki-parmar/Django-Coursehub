from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('registration', views.registration, name= 'registration'),
    path('dashboard/admin', views.admin_dashboard, name= 'admin_dashboard'),
    path('dashboard/instructor', views.instructor_dashboard, name= 'instructor_dashboard'),
    path('dashboard/student', views.student_dashboard, name= 'student_dashboard'),
]