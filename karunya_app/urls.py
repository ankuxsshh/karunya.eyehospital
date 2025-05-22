from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus', views.aboutus, name='aboutus'),
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
    path('lens', views.lens, name='lens'),
    path('treatments', views.treatments, name='treatments'),
    path('opt', views.opt, name='opt'),
    path('cataract', views.cataract, name='cataract'),
    path('retina', views.retina, name='retina'),
    path('laser', views.laser, name='laser'),
    path('intra', views.intra, name='intra'),
    path('store', views.store, name='store'),
    path('customer', views.customer, name='customer'),
]
