# Service provider delete profile
As a service provider I need to be  able to delete my profile.

## Priority: 40

## Estimation: 1 days
~5 hours with our budget.

## Assumptions:
- Only authenticated service providers can delete their profiles.

- Deleting a profile will also remove associated data, such as services and bookings (or mark them as inactive).

- A confirmation prompt will be required before deletion.

- Clients with existing bookings will be notified if a provider deletes their profile.

- The system will follow GDPR-compliant data deletion practices.

- Deleted accounts cannot be recovered.

## Description:
The system should provide a secure and efficient way for service providers to delete their profiles, ensuring that all relevant data is handled correctly.

## Tasks
1. Implement delete functionality for the ServiceProvider model.
2. Create an API endpoint for profile deletion.
3. Add a confirmation prompt before deletion.
4. Ensure that associated services and bookings are handled appropriately.
5. Send notifications to clients with existing bookings.
6. Document the delete profile feature.
7. Conduct unit and integration testing.
8. Implement front-end UI for the delete profile option.

# UI Design:

# Completed:
* (New, not in the textbook) 
* Insert screenshots of completed. 
* If you have multiple versions (changes between iteractions), show them all.

