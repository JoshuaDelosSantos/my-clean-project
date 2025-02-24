from django.urls import path
from . import views

urlpatterns = [
    path('sp_dashboard/', views.sp_dashboard, name='sp_dashboard'),
    path('sp_update_profile/', views.sp_update_profile, name='sp_update_profile'),
]