from django import forms
from .models import ServiceProvider, Availability

class ServiceProviderForm(forms.ModelForm):
    class Meta:
        model = ServiceProvider
        fields = ['name', 'email', 'contact_number',]

class ServiceProviderProfileForm(forms.ModelForm):
    class Meta:
        model = ServiceProvider
        fields = ['name',
                  'email',
                  'contact_number',
                  'address',
                  'city',
                  'state',
                  'post_code',
                  'description'
                ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'custom-input', 'placeholder': 'Business Name'}),
            'email': forms.EmailInput(attrs={'class': 'custom-input', 'placeholder': 'Email Address'}),
            'contact_number': forms.TextInput(attrs={'class': 'custom-input', 'placeholder': 'Contact Number'}),
            'address': forms.Textarea(attrs={'class': 'custom-textarea', 'rows': 1, 'placeholder': 'Street address'}),
            'city': forms.TextInput(attrs={'class': 'custom-input', 'placeholder': 'City'}),
            'state': forms.TextInput(attrs={'class': 'custom-input', 'placeholder': 'State'}),
            'post_code': forms.TextInput(attrs={'class': 'custom-input', 'placeholder': 'Post Code'}),
            'description': forms.Textarea(attrs={'class': 'custom-textarea', 'placeholder': 'Enter a description of your services'}),
        }
        
        

class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = Availability
        fields = ['start_time', 'end_time', 'description']

        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),  # Date and time picker for start_time
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),    # Date and time picker for end_time
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Availability description'}),  # Textarea for description
        }

