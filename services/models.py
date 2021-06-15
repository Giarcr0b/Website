from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Service(models.Model):

    class Meta:
        verbose_name_plural = 'services'

    name = models.CharField(max_length=80)
    title = models.CharField(max_length=200)
    description = models.TextField()
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(blank=True, null=True)
    order = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('services:detail', args=[self.pk])


class Component(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True)
    image_name = models.CharField(max_length=100)
    image_lnk = models.CharField(max_length=200)
    image_author = models.CharField(max_length=100)
    author_lnk = models.CharField(max_length=200)
    cc_license = models.CharField(max_length=80)
    cc_license_lnk = models.CharField(max_length=200)
    services = models.ManyToManyField(Service)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
