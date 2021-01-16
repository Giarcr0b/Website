from django.urls import path
from . import views

app_name = 'projects'
urlpatterns = [
    # path("", views.home, name="home"),
    path("", views.index, name="index"),
    path("<int:project_id>/", views.detail, name="detail"),
]