from django.db import models
from services.models import Service
from django.urls import reverse

# Create your models here.
class Testimonial(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    author = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Author(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    business = models.CharField(max_length=200)
    identity = models.TextField()
    why_work_with_me = models.TextField()
    why_hire_me = models.TextField()
    email = models.EmailField(max_length=256)
    mobile = models.CharField(max_length=40)
    about = models.TextField()
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.firstName

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30)
    service_list =  Service.objects.all()
    SERVICE_CHOICES = []
    for service in service_list:
        key = service.name
        title = service.name
        choice = (key, title)
        SERVICE_CHOICES.append(choice)

            
    
    type_of_service = models.CharField(choices=SERVICE_CHOICES, max_length=80)
    details = models.TextField()

    def get_absolute_url(self):
        return reverse('main:contact')