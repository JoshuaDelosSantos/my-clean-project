from django.urls import path
from . import views

urlpatterns = [
    path('', views.service_provider, name='service_provider'),
]