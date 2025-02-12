from django.urls import path
from . import views

urlpatterns = [
    path('', views.business_user, name='business_user'),
]