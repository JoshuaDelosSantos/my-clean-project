# Accounts app

## Table of Contents
- [Overview](#overview)
- [Endpoints](#endpoints)
- [Tests](#tests)

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

## Tests
The `tests.py` file contains unit tests for the views in this app:
- **`test_login_get`**: Checks if the service provider login page (`login_sp`) loads correctly via a GET request.
- **`test_register_sp_get`**: Checks if the service provider registration page (`register_sp`) loads correctly via a GET request.
- **`test_register_sp_post`**: Tests the service provider registration process with valid data via a POST request, ensuring a user is created and the user is redirected correctly.
- **`test_logout`**: Verifies that the logout view correctly logs out a logged-in user and redirects them to the homepage.

## [Back to main project folder](../../)