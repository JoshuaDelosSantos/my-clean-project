from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ServiceProvider
from forms import ServiceProviderProfileForm

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


@login_required
def sp_update_profile(request):
    """
    View function for updating the service provider profile.
    """
    
    service_provider = ServiceProvider.objects.get(user=request.user)
    
    if request.method == 'POST':
        form = ServiceProviderProfileForm(request.POST, instance=service_provider)
        if form.is_valid():
            form.save()
    else:
        form = ServiceProviderProfileForm(instance=service_provider)
    
    context = {
        'form': form
        }
    
    return render(request, 'service_provider/sp_update_profile.html', context)