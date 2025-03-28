from django.db import models
from django.contrib.auth.models import User

class ServiceProvider(models.Model):
    """
    Model representing a service provider.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    contact_number = models.CharField(max_length=15)
    address = models.TextField()
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=20)
    post_code = models.CharField(max_length=4)
    description = models.TextField()
    
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    service_provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.CharField(max_length=50)  # e.g., "9:00 AM - 10:00 AM"
    customer_name = models.CharField(max_length=100)
