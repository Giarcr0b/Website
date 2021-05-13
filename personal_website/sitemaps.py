from django.contrib import sitemaps
from django.urls import reverse
from services.models import Service
from projects.models import Project



class StaticViewSitemap(sitemaps.Sitemap):

    def items(self):
        return ['main:index', 'main:about', 'main:contact', 'main:testimonials', 'services:index', 'projects:index']

    def location(self, item):
        return reverse(item)

class ServicesSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Service.objects.all()

class ProjectsSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Project.objects.all()