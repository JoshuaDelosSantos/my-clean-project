from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from service_provider.models import ServiceProvider
from service_provider.categories import CleaningCategory

class CleaningServicesViewTests(TestCase):
    def setUp(self):
        """Set up test data for the cleaning services tests."""
        # Create test users first
        user1 = User.objects.create_user(username='testuser1', password='testpass1')
        user2 = User.objects.create_user(username='testuser2', password='testpass2')
        user3 = User.objects.create_user(username='testuser3', password='testpass3')
        
        # Create test service providers with different categories
        ServiceProvider.objects.create(
            user=user1,
            name="Test Cleaner 1",
            category=CleaningCategory.INDOOR.value,
            email="test1@example.com",
            contact_number="123-456-7890",
            city="Test City",
            description="Test description 1"
        )
        
        ServiceProvider.objects.create(
            user=user2,
            name="Test Cleaner 2",
            category=CleaningCategory.OUTDOOR.value,
            email="test2@example.com",
            contact_number="123-456-7891",
            city="Test City",
            description="Test description 2"
        )
        
        ServiceProvider.objects.create(
            user=user3,
            name="Test Cleaner 3",
            category=CleaningCategory.GENERAL.value,
            email="test3@example.com",
            contact_number="123-456-7892",
            city="Test City",
            description="Test description 3"
        )
    
    def test_view_url_accessible(self):
        """Test that the cleaning services view is accessible."""
        response = self.client.get(reverse('cleaning_services'))
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        """Test that the view uses the correct template."""
        response = self.client.get(reverse('cleaning_services'))
        self.assertTemplateUsed(response, 'cleaning_services/cleaning_services.html')
    
    def test_context_data(self):
        """Test that the view passes the correct context data."""
        response = self.client.get(reverse('cleaning_services'))
        self.assertTrue('objects' in response.context)
        self.assertTrue('categories' in response.context)
        self.assertTrue('selected_category' in response.context)
        self.assertEqual(response.context['selected_category'], 'all')
        
        # Check that all service providers are returned when no filter
        self.assertEqual(len(response.context['objects']), 3)
    
    def test_category_filtering(self):
        """Test that category filtering works correctly."""
        # Test INDOOR filter
        response = self.client.get(f"{reverse('cleaning_services')}?category={CleaningCategory.INDOOR.value}")
        self.assertEqual(len(response.context['objects']), 1)
        self.assertEqual(response.context['objects'][0].name, "Test Cleaner 1")
        self.assertEqual(response.context['selected_category'], CleaningCategory.INDOOR.value)
        
        # Test OUTDOOR filter
        response = self.client.get(f"{reverse('cleaning_services')}?category={CleaningCategory.OUTDOOR.value}")
        self.assertEqual(len(response.context['objects']), 1)
        self.assertEqual(response.context['objects'][0].name, "Test Cleaner 2")
        
        # Test GENERAL filter
        response = self.client.get(f"{reverse('cleaning_services')}?category={CleaningCategory.GENERAL.value}")
        self.assertEqual(len(response.context['objects']), 1)
        self.assertEqual(response.context['objects'][0].name, "Test Cleaner 3")
    
    def test_nonexistent_category(self):
        """Test filtering with a category that doesn't match any providers."""
        response = self.client.get(f"{reverse('cleaning_services')}?category=nonexistent")
        self.assertEqual(len(response.context['objects']), 0)
        self.assertEqual(response.context['selected_category'], "nonexistent")

