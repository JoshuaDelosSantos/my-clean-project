from django.contrib.auth.models import AbstractUser
from django.db import models

class Client(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    email = models.EmailField(unique=True)

    # Specify unique related_name to avoid clashes with default User model
    groups = models.ManyToManyField(
        'auth.Group', 
        related_name='client_set',  # Specify a unique reverse relation
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='client_set',  # Specify a unique reverse relation
        blank=True
    )

    def __str__(self):
        return f"{self.username} ({self.email})"
