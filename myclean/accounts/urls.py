from django.urls import path
from . import views

urlpatterns = [
    path('register_sp/', views.register_service_provider, name='register_sp'),
]