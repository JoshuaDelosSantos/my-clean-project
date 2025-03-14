from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import ServiceProvider

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
