from django.urls import path
from . import views

urlpatterns = [
    path('', views.cleaning_services, name='cleaning_services'),
]