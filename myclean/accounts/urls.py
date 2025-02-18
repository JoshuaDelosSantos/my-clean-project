from django.urls import path
from . import views

urlpatterns = [
    path('register_sp/', views.register_sp, name='register_sp'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]