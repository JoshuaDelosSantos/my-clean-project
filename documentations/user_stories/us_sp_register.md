# User story title: Service provider register
As a service provider I need to be able to register my service/s.

## Priority: 10

## Estimation: 3 days

## Assumptions:
- The service provider will register using an email andpassword.
- A verification email will be sent to confirm the registration.
- Basic profile details (e.g., business name, phone number, and location) will be required.
- Password must meet security standards (e.g., minimum 8characters, including a number and special character).
- Django’s built-in authentication system will be used 

## Description:
The service provider should be able to register for an account by providing essential information.

## Tasks
1. Create the User model with required fields.
2. Set up Django authentication.
3. Develop the registration form in Django view.
4. Implement input validation.
5. Create the registration API endpoint. 
6. Design a basic frontend page for registration.
7. Write test cases for user registration.

### Django steps:
1. Create 'users' app
Handles user registration and profile management.
- Models: Define User model and extend AbstractUser if needed.
- Views: Create registration logic and email verification.
- Forms: Use Django forms for validation.
- URLs: Set up routes for registration and verification.

2. Create 'authentication' app
Modular approach in seprating authentication logic from user management.
- Handle login, logout, password resets.
- Integrate Django's authentication system.

# UI Design:

# Completed:


