from django.shortcuts import render

# Create your views here.
def service_provider(request):
    return render(request, 'service_provider/service_provider.html', {})
