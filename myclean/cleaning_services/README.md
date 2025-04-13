# Cleaning Services App

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Category Filtering](#category-filtering)
- [Implementation](#implementation)
- [Tests](#tests)

## Overview
The **Cleaning Services** app is responsible for managing the services offered on the MyClean platform. It stores details about various services that clients can view and service providers can offer.

## Features
- Store and manage cleaning service categories
- Display a list of available cleaning services for clients
- Associate cleaning services with service providers
- Filter service providers by cleaning category (General, Indoor, Outdoor)

## Category Filtering
The platform now supports filtering service providers by their specialty:
- Service providers select their category during registration
- Categories are defined as an enumeration (General, Indoor, Outdoor)
- Users can filter providers based on the type of cleaning service they need
- The ServiceProvider model stores the selected category for each provider
- Providers can update their category from their dashboard as needed

## Implementation
The category system is implemented using:
- A `CleaningCategory` enum to ensure data consistency
- Integration with the ServiceProvider model
- Display of category information in the service provider dashboard

## Tests
The `tests.py` file contains unit tests for the `cleaning_services` view:
- **`setUp`**: Creates test users and service providers with different cleaning categories (Indoor, Outdoor, General) for testing purposes.
- **`test_view_url_accessible`**: Checks if the main `cleaning_services` view loads correctly (status code 200).
- **`test_view_uses_correct_template`**: Verifies that the view uses the `cleaning_services/cleaning_services.html` template.
- **`test_context_data`**: Ensures the view passes the correct context data (`objects`, `categories`, `selected_category`) and that all providers are shown by default.
- **`test_category_filtering`**: Tests if filtering by `INDOOR`, `OUTDOOR`, and `GENERAL` categories via GET parameters correctly returns only the relevant service providers.
- **`test_nonexistent_category`**: Checks that filtering with an invalid category returns no service providers.

## [Back to main project folder](../../)