from django.shortcuts import render
from service_provider.models import ServiceProvider


def cleaning_services(request):
    objects = ServiceProvider.objects.all()  # Returns a QuerySet of all objects
    return render(request, 'cleaning_services/cleaning_services.html', {"objects": objects})


