from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ServiceProvider

@login_required
def sp_dashboard(request):
    """
    View function for the service provider dashboard.
    """
    
    service_provider = ServiceProvider.objects.get(user=request.user)
    context = {
        'service_provider': service_provider
        }
    
    return render(request, 'service_provider/sp_dashboard.html', context)
