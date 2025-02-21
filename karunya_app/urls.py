from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('appoinment', views.appoinment, name='appoinment'),    
    path('department', views.department, name='department'),   
    path('doctor', views.doctor, name='doctor'),   
    path('gallery', views.gallery, name='gallery'),   
    path('doctor-single', views.doctorsingle, name='doctor-single'), 

]
