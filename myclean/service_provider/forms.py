from django import forms
from .models import ServiceProvider

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
            'address': forms.Textarea(attrs={'rows': 1, 'placeholder': 'Street address'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter a description of your services'}),
        }
        