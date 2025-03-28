from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ServiceProvider, Booking
from .forms import ServiceProviderProfileForm
import calendar
from datetime import datetime


@login_required
def sp_dashboard(request):
    """
    View function for the service provider dashboard.
    """
    
    service_provider = ServiceProvider.objects.get(user=request.user)
    
    context = {
        'service_provider': service_provider
        }
    
    
    # Get the current date
    current_date = datetime.now()
    
     # Format the date to display as 'Month Year'
    formatted_date = current_date.strftime('%B %Y')
    
    # Generate a list of days in the current month (7x4 grid: Sun-Sat)
    month_days = calendar.monthcalendar(current_date.year, current_date.month)
    
    # Get existing bookings for this service provider
    bookings = Booking.objects.filter(service_provider=service_provider, date__month=current_date.month)
    
    context = {
        'service_provider': service_provider,
        'month_days': month_days,
        'bookings': bookings,
        'formatted_date': formatted_date,  # Pass the formatted date to the template
        # 'current_date': current_date,
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