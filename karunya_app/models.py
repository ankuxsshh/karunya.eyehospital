# models.py

from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=100, default='')
    message = models.TextField()
    image = models.ImageField(upload_to='testimonials/')
    rating = models.IntegerField(default=5)  # Rating out of 5
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.rating} Stars"


class InsuranceCompany(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
