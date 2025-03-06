import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myclean.settings") 
django.setup()

import random
from faker import Faker
from django.contrib.auth.models import User
from service_provider.models import ServiceProvider

fake = Faker()

def create_mock_service_providers(n=10):
    for _ in range(n):
        # Create a User instance
        user = User.objects.create_user(
            username=fake.user_name(),
            email=fake.email(),
            password="password123"  # Default password
        )

        # Create the ServiceProvider instance
        ServiceProvider.objects.create(
            user=user,
            name=fake.company(),
            email=user.email,
            contact_number=fake.phone_number()[:10],
            address=fake.address(),
            city=fake.city(),
            state=fake.state(),
            post_code=fake.postcode()[:4],  # Ensuring 4-digit postcode
            description=fake.text(),
            is_verified=random.choice([True, False])
        )

    print(f"Successfully created {n} mock service providers.")

if __name__ == "__main__":
    create_mock_service_providers(10)  # Adjust number as needed