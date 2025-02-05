from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # This will display the home page at the root URL
]