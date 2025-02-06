from django.urls import path
from . import views

urlpatterns = [
    path('cleaning_services', views.cleaning_services, name='cleaning_services'),
]