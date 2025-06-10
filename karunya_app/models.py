# models.py

from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=100, default='')
    title = models.CharField(max_length=150)
    message = models.TextField()
    image = models.ImageField(upload_to='testimonials/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.title}"


class InsuranceCompany(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
