from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from service_provider.forms import ServiceProviderForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout


def register_sp(request):
    """
    View function for registering a service provider.
    """
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        service_provider_form = ServiceProviderForm(request.POST)
        if user_form.is_valid() and service_provider_form.is_valid():
            user = user_form.save()
            service_provider = service_provider_form.save(commit=False)
            service_provider.user = user
            service_provider.save()
            login(request, user)
            return redirect('sp_dashboard')
    else:
        user_form = UserCreationForm()
        service_provider_form = ServiceProviderForm()
    
    context = {
        'user_form': user_form,
        'service_provider_form': service_provider_form
    }
    return render(request, 'accounts/register_sp.html', context)

def logout_view(request):
    """
    View function for logging out a user.
    """
    logout(request)
    return redirect('home')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)  # Use Django's built-in form
        if form.is_valid():
            user = form.get_user()  # Get the authenticated user
            login(request, user)  # Log the user in
            return redirect('sp_dashboard')  # Redirect to a home page or dashboard
    else:
        form = AuthenticationForm()  # Display an empty form for GET requests

    return render(request, 'accounts/login.html', {'form': form})