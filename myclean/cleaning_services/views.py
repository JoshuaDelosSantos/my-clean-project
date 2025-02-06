from django.shortcuts import render

def cleaning_services(request):
    return render(request, 'cleaning_services/cleaning_services.html', {})
