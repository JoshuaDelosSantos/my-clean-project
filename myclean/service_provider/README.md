# Service provider app

## Table of Contents
- [Overview](#overview)
- [Model](#model)
- [Availability](#availability)
- [Forms](#forms)
- [Endpoints](#endpoints)
- [Testing](#testing)

## Overview:
The **Service Provider** app is responsible for managing service providers on the MyClean platform. It includes models, forms, views, and templates for creating and managing service provider profiles.

## Model
Defines the ServiceProvider model, which extends Django's built-in User model using a OneToOneField relationship. 
Service Providers must be linked to a User account.

### Usage:
To create a new service provider, you need to:
1. Create a Django User object.
2. Create a ServiceProvider object and link it to the User.

### Example:
```python
from django.contrib.auth.models import User
from service_provider.models import ServiceProvider
from service_provider.categories import CleaningCategory

# Create a User
user = User.objects.create_user(username="provider1", password="securepassword")

# Create a Service Provider linked to the User
provider = ServiceProvider.objects.create(
    user=user,
    name="John's Cleaning",
    email="john@example.com",
    contact_number="1234567890",
    address="123 Main Street",
    city="Townsville",
    state="QLD",
    post_code="4810",
    description="Professional cleaning services.",
    category=CleaningCategory.INDOOR.value
)

print(provider.name)  # Output: John's Cleaning
```

## Availability
The app includes an `AvailabilitySlot` model that allows service providers to manage their availability.

### AvailabilitySlot model:
- Tracks dates when service providers are available
- Connected to a ServiceProvider via a ForeignKey relationship
- Contains date and availability status fields

### Example:
```python
from service_provider.models import ServiceProvider, AvailabilitySlot
from datetime import date

# Get existing service provider
provider = ServiceProvider.objects.get(name="John's Cleaning")

# Add availability for today
slot = AvailabilitySlot.objects.create(
    service_provider=provider,
    date=date.today(),
    is_available=True
)
```

## Forms:
### ServiceProviderForm:
- A form for creating a 'ServiceProvider' instance.

**Fields:**
- 'name' 
- 'email' 
- 'contact_number'

### ServiceProviderProfileForm:
- A form for updating the ServiceProvider's profile.

**Fields:**
- 'name'
- 'category'
- 'email'
- 'contact_number'
- 'address'
- 'city'
- 'state'
- 'post_code'
- 'description'


## Endpoints:
### 'service_provider/sp_dashboard/'
- Displays logged in service_provider user's profile.

### 'service_provider/sp_update_profile/'
- Uses ServiceProviderProfileForm and allows user to update their profile.
- User is then redirected to dashboard after completion.

### 'service_provider/sp_availability/'
- Displays the availability calendar for the service provider.
- Shows current availability slots by date.

### 'service_provider/sp_add_availability/'
- Form for adding new availability slots.
- Redirects to availability view upon successful creation.

### 'service_provider/sp_delete_availability/<slot_id>/'
- Deletes a specific availability slot.
- Redirects to availability view after deletion.

### 'service_provider/booking/<slot_id>/'
- Displays a booking form for a specific availability slot.
- Handles POST requests to create a new booking and marks the slot as unavailable.

## Testing
The `tests.py` file includes comprehensive test coverage for views and functionality:

### Service Provider View Tests (`ServiceProviderViewTests`)
- **Dashboard Access**: Tests `sp_dashboard` view for logged-in users and redirection for unauthenticated users.
- **Profile Update**: Tests `sp_update_profile` view (GET and POST), ensuring profile data is updated correctly and redirects to the dashboard.
- **Availability Management**:
    - **View Availability**: Tests `sp_availability` view for logged-in users, checking context data (calendar, slots).
    - **Add Availability**: Tests `sp_add_availability` view (GET and POST), verifying slot creation and redirection.
    - **Delete Availability**: Tests `sp_delete_availability` view (POST), ensuring slots are deleted and redirection occurs.

### Booking Form Tests (`BookingFormTests`)
- **Form Display**: Tests if the `booking_form` view loads correctly (GET).
- **Valid Booking**: Tests successful booking submission (POST), verifying booking creation, slot unavailability, and redirection.
- **Double Booking Prevention**: Ensures that attempting to book an already booked slot fails and displays an appropriate message.

All tests can be run using Django's test runner:
```bash
python manage.py test service_provider
```

## [Back to main project folder](../../)