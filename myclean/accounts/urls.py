from django.urls import path
from . import views

urlpatterns = [
    path('register_sp/', views.register_sp, name='register_sp'),
]