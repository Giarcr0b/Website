from django.db import models

# Create your models here.
class Service(models.Model):

    class Meta:
        verbose_name_plural = 'services'

    name=models.CharField(max_length=80)
    title=models.CharField(max_length=200)
    description=models.TextField()
    rate=models.DecimalField(max_digits=5, decimal_places=2)
    image=models.ImageField(blank=True, null=True)
    order=models.IntegerField()

    def __str__(self):
        return self.name


class Component(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField()
    services = models.ManyToManyField(Service)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name