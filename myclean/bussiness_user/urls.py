from django.urls import path
from . import views

urlpatterns = [
    path('', views.bussiness_user, name='bussiness_user'),
]