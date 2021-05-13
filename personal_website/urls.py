"""personal_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin, sitemaps
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from personal_website import settings
from .sitemaps import StaticViewSitemap, ProjectsSitemap, ServicesSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'services': ServicesSitemap,
    'projects': ProjectsSitemap,
    
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path("", include("main.urls")),
    path("projects/", include("projects.urls")),
    path("blog/", include("blog.urls")),
    path("services/", include("services.urls")),
    path('captcha/', include('captcha.urls')),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

""" path("", include("main.urls")),
    path("projects/", include("projects.urls")),
    path("blog/", include("blog.urls")),
    path("services/", include("services.urls")), """