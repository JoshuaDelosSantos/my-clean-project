from django.urls import path
from . import views

urlpatterns = [
    path('service_provider/', views.register_service_provider, name='register_service_provider'),
]