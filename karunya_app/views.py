from django.shortcuts import render
from .models import Testimonial, InsuranceCompany

# Create your views here.

def index(request):
    testimonials = Testimonial.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'testimonials': testimonials})

def about(request):
    return render(request, 'about.html')

def managements(request):
    return render(request, 'managements.html')

def services(request):
    return render(request, 'services.html')

def department(request):
    return render(request, 'department.html')

def contactform(request):
    return render(request, 'contactform.html')

def appoinment(request):
    return render(request, 'appoinment.html')

def doctor(request):
    return render(request, 'doctor.html')

def gallery(request):
    return render(request, 'gallery.html')

def doctorsingle(request):
    return render(request, 'doctor-single.html')

def specialities(request):
    return render(request, 'specialities.html') 

def eyeproblem(request):
    return render(request, 'eyeproblem.html')

def centres(request):
    return render(request, 'centres.html')

def insurances(request):
    insurances = InsuranceCompany.objects.all()
    return render(request, 'insurances.html', {'insurances': insurances})

def events(request):    
    return render(request, 'events.html')

def treatments(request):
    return render(request, 'treatments.html')