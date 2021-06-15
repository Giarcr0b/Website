"""personal_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.urls import path
from main import views


app_name = 'main'
urlpatterns = [
    path("", views.indexView.as_view(), name="index"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("contact_form/", views.ContactView.as_view(), name="contact"),
    path("testimonials/", views.TestimonialView.as_view(), name="testimonials"),
    path("get_in_touch/", views.get_in_touch, name="get_in_touch"),
    path("get_in_touch_confirm/", views.get_in_touch_confirm, name="confirm"),
]
