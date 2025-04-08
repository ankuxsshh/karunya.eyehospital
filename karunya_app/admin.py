from django.contrib import admin
from .models import Testimonial, InsuranceCompany
from django.contrib.auth.models import User, Group
    
admin.site.register(Testimonial)
admin.site.register(InsuranceCompany)

# Unregister User and Group from the admin panel
admin.site.unregister(User)
admin.site.unregister(Group)