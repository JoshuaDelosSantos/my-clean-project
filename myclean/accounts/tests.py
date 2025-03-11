from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class AccountsViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login_get(self):
        # GET request for login view
        response = self.client.get(reverse('login_sp')) 
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login_sp.html')

    def test_register_sp_get(self):
        # GET request for service provider registration view
        response = self.client.get(reverse('register_sp'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register_sp.html')

    def test_register_sp_post(self):
        # POST request for a successful registration
        data = {
            'username': 'testuser',
            'password1': 'StrongPass123',
            'password2': 'StrongPass123',
            'name': 'Test User',
            'email': 'test@user.com',
            'contact_number': '1234567890'
        }
        response = self.client.post(reverse('register_sp'), data)
        self.assertTrue(User.objects.filter(username='testuser').exists())
        self.assertRedirects(response, reverse('sp_dashboard'))

    def test_logout(self):
        # Test logout view redirection
        user = User.objects.create_user(username='testuser', password='StrongPass123')
        self.client.login(username='testuser', password='StrongPass123')
        response = self.client.get(reverse('logout'))  # update URL name if needed
        self.assertRedirects(response, reverse('cleaning_services'))  # update URL name if needed
