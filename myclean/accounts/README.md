# Accounts app

## Overview:
Responsible for registration, login & logout.

## Endpoints:
### 'accounts/register_sp/'
- Displays a registration form for new service providers.
- Handles form submission and creates a new user and initial service provider profile.
- Redirects user to 'service_provider/sp_dashboard'.

### 'accounts/login_sp/'
- Displays login form for service providers.
- Redirects user to service provider dashboard if login credentials are valid.

### 'accounts/logout/'
- Logs out user and redirects to homepage.