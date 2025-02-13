# Service provider app

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
```
from django.contrib.auth.models import User
from service_provider.models import ServiceProvider

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
    description="Professional cleaning services."
)

print(provider.name)  # Output: John's Cleaning
```

## Forms:
### ServiceProviderForm:
- A form for creating and 'ServiceProvider' instance.

**Fields:**
- 'name' 
- 'email' 
- 'contact_number'


## Endpoints:
**'service_provider/sp_dashboard/'**
- Displays logged in service_provider user's profile.

