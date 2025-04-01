from django.db import models
from django.contrib.auth.models import User
from .categories import CleaningCategory
from .models import AvailabilitySlot

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
    category = models.CharField(
        max_length=15,
        choices=[(category.value, category.value) for category in CleaningCategory],
        default=CleaningCategory.GENERAL.value
    )
    
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class AvailabilitySlot(models.Model):
    service_provider = models.ForeignKey('ServiceProvider', on_delete=models.CASCADE, related_name='availability_slots')
    date = models.DateField()
    is_available = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return f"{self.service_provider.name}: {self.date}"

class Booking(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    availability_slot = models.OneToOneField(AvailabilitySlot, on_delete=models.CASCADE)
    additional_notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client.username} booked {self.availability_slot}"