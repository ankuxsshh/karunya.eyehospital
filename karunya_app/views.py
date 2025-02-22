from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def department(request):
    return render(request, 'department.html')

def contact(request):
    return render(request, 'contact.html')

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
