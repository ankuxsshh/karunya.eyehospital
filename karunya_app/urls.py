from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('managements', views.managements, name='managements'),
    path('services', views.services, name='services'),
    path('contactform', views.contactform, name='contactform'),
    path('appoinment', views.appoinment, name='appoinment'),    
    path('department', views.department, name='department'),   
    path('doctor', views.doctor, name='doctor'),   
    path('gallery', views.gallery, name='gallery'),   
    path('doctor-single', views.doctorsingle, name='doctor-single'), 
    path('specialities', views.specialities, name='specialities'), 
    path('eyeproblem', views.eyeproblem, name='eyeproblem'),
    path('centres', views.centres, name='centres'),
    path('insurances', views.insurances, name='insurances'),
    path('events', views.events, name='events'),

]
