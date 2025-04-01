from django.urls import path
from . import views

urlpatterns = [
    path('sp_dashboard/', views.sp_dashboard, name='sp_dashboard'),
    path('sp_update_profile/', views.sp_update_profile, name='sp_update_profile'),
    path('sp_availability/', views.sp_availability, name='sp_availability'),
    path('sp_add_availability/', views.sp_add_availability, name='sp_add_availability'),
    path('sp_delete_availability/<int:slot_id>/', views.sp_delete_availability, name='sp_delete_availability'),
    path('book/<int:slot_id>/', views.booking_form, name='booking_form'),
]