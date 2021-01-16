from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    # path("", views.home, name="home"),
    path("", views.IndexView.as_view(), name="index"),
    path("<int:service_id>/", views.detail, name="detail"),
]