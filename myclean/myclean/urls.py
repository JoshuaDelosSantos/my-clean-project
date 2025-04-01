"""
URL configuration for myclean project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from service_provider.views import booking_form

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('home.urls')),  # This will include the home app's URLs
    path('', include('cleaning_services.urls')),
    path('accounts/', include('accounts.urls')),
    path('service_provider/', include('service_provider.urls')),
    path('book/<int:slot_id>/', booking_form, name='booking_form'),
]
