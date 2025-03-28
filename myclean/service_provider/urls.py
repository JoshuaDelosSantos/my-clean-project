from django.urls import path
from . import views

urlpatterns = [
    path('sp_dashboard/', views.sp_dashboard, name='sp_dashboard'),
    path('sp_update_profile/', views.sp_update_profile, name='sp_update_profile'),
    
    path('sp_get_schedule/', views.get_schedule, name='get_schedule'),  # For fetching events
    path('sp_add_schedule/', views.add_schedule, name='add_schedule'),  # For adding new events
    path('sp_edit_schedule/<int:event_id>/', views.edit_schedule, name='edit_schedule'),  # For editing events
]

