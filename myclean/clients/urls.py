from django.urls import path
from . import views

urlspatterns = [
    path['clients/', views.clients, name='clients']
]