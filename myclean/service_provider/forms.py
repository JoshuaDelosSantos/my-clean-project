from django import forms
from .models import ServiceProvider
from .models import Booking


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

class AvailabilityForm(forms.Form):
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    availability = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter your availability for each day.'}))

