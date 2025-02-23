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
        