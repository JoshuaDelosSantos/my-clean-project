# Application Architecture

[← Back to Project Root](../)

## Table of Contents
- [Django Pattern](#django-pattern)
- [MVT Pattern Explained](#mvt-pattern-explained)
  - [Model](#model)
  - [View](#view)
  - [Template](#template)
  - [Request Flow](#request-flow)
  - [Project Structure](#project-structure)
  - [Best Practices](#best-practices)
- [App Architecture](#app-architecture)
  - [PostgreSQL Integration](#postgresql-integration)
  - [Accounts App](#accounts-app)
  - [Service Provider App](#service-provider-app)
  - [Cleaning Services App](#cleaning-services-app)
  - [App Relationships](#app-relationships)

## Django Pattern
![Django Pattern Diagram](/documentations/screenshots/django-pattern.png)
- Django follows the MVT pattern:
    - M: Model
    - V: View
    - T: Template

## MVT Pattern Explained
Django implements a Model-View-Template (MVT) architecture, a variant of the MVC pattern:

### Model
- Represents the data structure and business logic
- Implemented as Python classes that inherit from `django.db.models.Model`
- Handles database interactions through Django's ORM
- Provides field validation, relationships, and query capabilities

### View
- Processes HTTP requests and returns HTTP responses
- Retrieves data from models and passes it to templates
- Handles user input and forms
- Can be implemented as functions or class-based views

### Template
- Defines the presentation layer using Django's template language
- Combines HTML with template tags and filters
- Receives context data from views for rendering
- Supports template inheritance for consistent layouts

### Request Flow
1. URL dispatcher receives a request and routes it to the appropriate view
2. View processes the request, interacts with models if needed
3. View renders a template with context data
4. Response is sent back to the client

### Project Structure
- **Settings**: Configuration for database, installed apps, middleware, etc.
- **URLs**: URL routing configuration
- **WSGI/ASGI**: Entry points for web servers
- **Apps**: Modular components of functionality (each with models, views, templates)
- **Middleware**: Request/response processing layers

### Best Practices
- Keep apps small and focused on specific functionality
- Use class-based views for complex views
- Leverage Django's built-in security features
- Follow Django's "fat models, thin views" philosophy
- Use Django REST Framework for API development

## App Architecture
![Applications Architecture Diagram](/documentations/screenshots/apps-architecture.png)

The MyClean project consists of three primary apps that follow the MVT pattern, with each connected to PostgreSQL for data persistence:

### PostgreSQL Integration
All three apps connect to a centralized PostgreSQL database configured in `settings.py`:
- Connection parameters are managed via environment variables for security
- Django's ORM translates Python objects to database tables and queries
- Migrations handle schema creation and updates across all apps
- Each app's models are converted to dedicated database tables with proper relationships

### Accounts App
**Models:**
- Leverages Django's built-in `User` model for authentication
- No additional custom models, instead relies on User-ServiceProvider relationship

**Views:**
- `LoginInterfaceView`: Class-based view handling service provider login
- `register_sp`: Function-based view for service provider registration
- `logout_view`: Simple view for user logout

**Templates:**
- `login_sp.html`: Login form for service providers
- `register_sp.html`: Registration form for new service providers

### Service Provider App
**Models:**
- `ServiceProvider`: Extends User with profile information (name, contact details, category)
- `AvailabilitySlot`: Stores provider availability dates
- `Booking`: Links clients to availability slots for appointments

**Views:**
- `sp_dashboard`: Shows provider profile overview
- `sp_update_profile`: Handles profile editing
- `sp_availability`: Calendar-based availability management
- `booking_form`, `booking_success`: Client booking functionality

**Templates:**
- `sp_dashboard.html`: Provider's main interface
- `sp_update_profile.html`: Profile editing form
- `sp_availability.html`: Calendar-based availability interface
- `booking_form.html`, `booking_success.html`: Booking workflow templates

### Cleaning Services App
**Models:**
- No custom models, instead queries the ServiceProvider model

**Views:**
- `cleaning_services`: Main view that displays all services with filtering options

**Templates:**
- `cleaning_services.html`: Lists all available service providers with filtering controls

### App Relationships
The diagram illustrates how these three apps form a composition relationship with Django's MVT components:
- Each app contributes its own Models, Views, and Templates
- The apps interact with each other through model relationships
- Service Provider models are referenced by both Accounts (for authentication) and Cleaning Services (for listing)
- All data operations are ultimately persisted to the PostgreSQL database

## [Back to main project folder](../)