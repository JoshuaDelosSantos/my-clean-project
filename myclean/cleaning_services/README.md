# Cleaning Services App

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