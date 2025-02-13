from django.urls import path
from . import views

urlpatterns = [
    path('sp_dashboard/', views.sp_dashboard, name='sp_dashboard'),
]