from django.shortcuts import render
from service_provider.models import ServiceProvider
from service_provider.categories import CleaningCategory

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
    
    context = {
        "objects": queryset,
        "categories": categories,
        "selected_category": category_filter or 'all'
    }
    
    return render(request, 'cleaning_services/cleaning_services.html', context)


