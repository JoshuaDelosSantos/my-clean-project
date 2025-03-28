from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ServiceProvider
from .forms import ServiceProviderProfileForm
from django.http import JsonResponse
from .models import Availability
from .forms import AvailabilityForm


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
            return redirect('sp_dashboard')
    else:
        form = ServiceProviderProfileForm(instance=service_provider)
    
    context = {
        'form': form
        }
    
    return render(request, 'service_provider/sp_update_profile.html', context)



@login_required
def get_schedule(request):
    """
    View to fetch all the availability events for the logged-in service provider.
    """
    service_provider = ServiceProvider.objects.get(user=request.user)
    availability = Availability.objects.filter(service_provider=service_provider)

    events = []
    for item in availability:
        events.append({
            'id': item.id,
            'title': f"{item.service_provider.name} Available",
            'start': item.date.isoformat() + 'T' + item.start_time.strftime('%H:%M:%S'),
            'end': item.date.isoformat() + 'T' + item.end_time.strftime('%H:%M:%S'),
        })
    
    return JsonResponse(events, safe=False)



@login_required
def add_schedule(request):
    """
    View to add a new schedule item (availability).
    """
    if request.method == 'POST':
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            availability = form.save(commit=False)
            availability.service_provider = ServiceProvider.objects.get(user=request.user)
            availability.save()
            return redirect('sp_dashboard')
    else:
        form = AvailabilityForm()

    return render(request, 'service_provider/add_schedule.html', {'form': form})



@login_required
def edit_schedule(request, event_id):
    """
    View to edit an existing schedule item.
    """
    availability = Availability.objects.get(id=event_id, service_provider__user=request.user)
    
    if request.method == 'POST':
        form = AvailabilityForm(request.POST, instance=availability)
        if form.is_valid():
            form.save()
            return redirect('sp_dashboard')
    else:
        form = AvailabilityForm(instance=availability)
    
    return render(request, 'service_provider/edit_schedule.html', {'form': form})
