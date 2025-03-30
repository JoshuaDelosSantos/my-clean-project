from django.shortcuts import render
from service_provider.models import ServiceProvider, AvailabilitySlot
from service_provider.categories import CleaningCategory
from datetime import datetime, timedelta

def cleaning_services(request):
    # Get the category filter from query parameters (if any)
    category_filter = request.GET.get('category', None)
    
    # Start with all objects
    queryset = ServiceProvider.objects.all()
    
    # Apply filter if a category is specified
    if category_filter and category_filter != 'all':
        queryset = queryset.filter(category=category_filter)
    
    # Get all available categories for the filter dropdown
    categories = [category.value for category in CleaningCategory]
    
    # Get available slots for each provider
    providers_with_availability = {}
    for provider in queryset:
        next_week_slots = AvailabilitySlot.objects.filter(
            service_provider=provider,
            date__gte=datetime.today().date(),
            date__lte=datetime.today().date() + timedelta(days=7),
            is_available=True
        ).order_by('date') 
        providers_with_availability[provider.id] = next_week_slots
    
    context = {
        "objects": queryset,
        "categories": categories,
        "selected_category": category_filter or 'all',
        "providers_availability": providers_with_availability  # Variable name matches what we're using
    }
    
    return render(request, 'cleaning_services/cleaning_services.html', context)


