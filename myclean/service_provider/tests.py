from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import ServiceProvider, AvailabilitySlot
from .categories import CleaningCategory
from datetime import date

class ServiceProviderViewTests(TestCase):
    def setUp(self):
        # Create a test user and corresponding service provider
        self.client = Client()
        self.user = User.objects.create_user(username='testsp', password='testpass')
        self.service_provider = ServiceProvider.objects.create(user=self.user)
    
    def login(self):
        self.client.login(username='testsp', password='testpass')

    def test_sp_dashboard_get(self):
        # Ensure redirection if not logged in
        response = self.client.get(reverse('sp_dashboard'))
        self.assertNotEqual(response.status_code, 200)

        # Login and test dashboard view
        self.login()
        response = self.client.get(reverse('sp_dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('service_provider', response.context)
    
    def test_sp_update_profile_get(self):
        # Ensure redirection if not logged in
        response = self.client.get(reverse('sp_update_profile'))
        self.assertNotEqual(response.status_code, 200)

        # Login and test update profile view (GET)
        self.login()
        response = self.client.get(reverse('sp_update_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)

    def test_sp_update_profile_post(self):
        self.login()
        post_data = {
            'name': 'Test SP',
            'category': CleaningCategory.GENERAL.value,
            'email': 'testsp@example.com',
            'contact_number': '1234567890',
            'address': '123 Main St',
            'city': 'Test City',
            'state': 'Test State',
            'post_code': '1234',
            'description': 'Updated bio information',
        }
        response = self.client.post(reverse('sp_update_profile'), data=post_data)
        
        # Assert that it gets redirected to the dashboard after succesful update of the profile
        self.assertEqual(response.status_code, 302)  
        self.assertEqual(response.url, reverse('sp_dashboard'))
        self.service_provider.refresh_from_db()
        self.assertEqual(self.service_provider.description, 'Updated bio information')
    
    def test_sp_availability_get(self):
        # Ensure redirection if not logged in
        response = self.client.get(reverse('sp_availability'))
        self.assertNotEqual(response.status_code, 200)
        
        # Login and test availability view
        self.login()
        response = self.client.get(reverse('sp_availability'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('service_provider', response.context)
        self.assertIn('calendar', response.context)
        self.assertIn('availability_by_date', response.context)
    
    def test_sp_add_availability_get(self):
        # Ensure redirection if not logged in
        response = self.client.get(reverse('sp_add_availability'))
        self.assertNotEqual(response.status_code, 200)
        
        # Login and test add availability view (GET)
        self.login()
        response = self.client.get(reverse('sp_add_availability'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)
        self.assertIn('service_provider', response.context)
    
    def test_sp_add_availability_post(self):
        self.login()
        today = date.today()
        post_data = {
            'date': today,
            'is_available': True
        }
        response = self.client.post(reverse('sp_add_availability'), data=post_data)
        
        # Assert redirection after successful slot creation
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('sp_availability'))
        
        # Assert that slot was created
        self.assertEqual(
            AvailabilitySlot.objects.filter(
                service_provider=self.service_provider,
                date=today
            ).count(), 
            1
        )
    
    def test_sp_delete_availability(self):
        self.login()
        # Create a slot to delete
        slot = AvailabilitySlot.objects.create(
            service_provider=self.service_provider,
            date=date.today(),
            is_available=True
        )
        
        response = self.client.post(reverse('sp_delete_availability', args=[slot.id]))
        
        # Assert redirection after deletion
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('sp_availability'))
        
        # Assert that slot was deleted
        self.assertEqual(
            AvailabilitySlot.objects.filter(id=slot.id).count(),
            0
        )
