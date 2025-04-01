from django import forms
from .models import ServiceProvider, AvailabilitySlot, Booking

class ServiceProviderForm(forms.ModelForm):
    class Meta:
        model = ServiceProvider
        fields = ['name', 'email', 'contact_number',]

class ServiceProviderProfileForm(forms.ModelForm):
    class Meta:
        model = ServiceProvider
        fields = ['name',
                  'category',
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
            'category': forms.Select(attrs={'class': 'custom-select custom-input', 'placeholder': 'Select Category'}),
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
        model = AvailabilitySlot
        fields = ['date', 'is_available']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'custom-input'}),
        }

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['availability_slot', 'name', 'email', 'phone', 'additional_notes']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['availability_slot'].queryset = AvailabilitySlot.objects.filter(is_available=True)
