from django.urls import path
from . import views

urlpatterns = [
    path('sp_dashboard/', views.service_provider_dashboard, name='sp_dashboard'),
]