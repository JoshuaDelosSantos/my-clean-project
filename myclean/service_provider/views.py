from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ServiceProvider, AvailabilitySlot, Booking
from .forms import ServiceProviderProfileForm, AvailabilityForm, BookingForm
from django.contrib import messages
from datetime import datetime, timedelta
import calendar

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
def sp_availability(request):
    """
    View function for managing service provider availability.
    """
    service_provider = ServiceProvider.objects.get(user=request.user)
    
    # Get current month and year
    today = datetime.today()
    current_month = today.month
    current_year = today.year
    
    # Get all days in the current month
    cal = calendar.monthcalendar(current_year, current_month)
    
    # Get all availability slots for this service provider
    availability_slots = AvailabilitySlot.objects.filter(
        service_provider=service_provider,
        date__month=current_month,
        date__year=current_year
    )
    
    # Organize availability by date
    availability_by_date = {}
    for slot in availability_slots:
        date_str = slot.date.strftime('%Y-%m-%d')
        if date_str not in availability_by_date:
            availability_by_date[date_str] = []
        availability_by_date[date_str].append(slot)
    
    # Format the calendar with date strings
    formatted_calendar = []
    for week in cal:
        formatted_week = []
        for day in week:
            if day != 0:
                # Format the date string here instead of in the template
                date_str = f"{current_year}-{current_month:02d}-{day:02d}"
                formatted_week.append({'day': day, 'date_str': date_str})
            else:
                formatted_week.append({'day': 0, 'date_str': ''})
        formatted_calendar.append(formatted_week)
    
    context = {
        'service_provider': service_provider,
        'calendar': formatted_calendar,
        'month': current_month,
        'year': current_year,
        'month_name': calendar.month_name[current_month],
        'availability_by_date': availability_by_date,
    }
    
    return render(request, 'service_provider/sp_availability.html', context)

@login_required
def sp_add_availability(request):
    """
    View function for adding new availability slots.
    """
    service_provider = ServiceProvider.objects.get(user=request.user)
    
    if request.method == 'POST':
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            slot = form.save(commit=False)
            slot.service_provider = service_provider
            slot.save()
            messages.success(request, 'Availability slot added successfully!')
            return redirect('sp_availability')
    else:
        form = AvailabilityForm()
    
    context = {
        'form': form,
        'service_provider': service_provider
    }
    
    return render(request, 'service_provider/sp_add_availability.html', context)

@login_required
def sp_delete_availability(request, slot_id):
    """
    View function for deleting an availability slot.
    """
    service_provider = ServiceProvider.objects.get(user=request.user)
    slot = get_object_or_404(AvailabilitySlot, id=slot_id, service_provider=service_provider)
    
    slot.delete()
    messages.success(request, 'Availability slot deleted successfully!')
    return redirect('sp_availability')

def booking_form(request, slot_id):
    if request.method == "POST":
        form = BookingForm(request.POST)
        print(f"Form is valid: {form.is_valid()}")  # Check if form is valid
        if form.is_valid():
            booking = form.save(commit=False)
            # Fetch the slot object from the database
            slot = AvailabilitySlot.objects.get(id=slot_id)
            
            if request.user.is_authenticated:
                booking.client = request.user
            else:
                booking.client = None
            
            booking.slot = slot  # Assign the slot to the booking
            booking.save()
            
            # Mark the slot as unavailable after booking
            slot.is_available = False
            slot.save()
            
            print("Form is valid, redirecting to booking success")
            return redirect("booking_success")
        else:
            print("Form is not valid")
    else:
        form = BookingForm()

    return render(request, "booking_form.html", {"form": form})



def booking_success(request):
    return render(request, 'booking_success.html')
