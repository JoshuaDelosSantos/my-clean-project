from django.urls import path
from . import views

urlpatterns = [
    path('register_sp/', views.register_sp, name='register_sp'),
    path('login_sp/', views.LoginInterfaceView.as_view(), name='login_sp'),
    path('logout/', views.logout_view, name='logout'),
]