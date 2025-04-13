# CP3407 - Project

## Overview:
This a project assignment for CP3407. 
The main task was to create a software for individual cleaners and cleaning companies to manage their booking/s.

## Team
1. Callum Riley
2. Jackson Doyle
3. Reece Kelly
4. Joshua Delos Santos

## Project planning:
- Have a shared understanding of the project.
- Define the 'budget' for this project.
- Decide on the software lifecycle development framework to follow.
- User stories.
- Discuss about the tech stack.
- Talk about resources (LinkedIn Learning).
- Set up VS Code and make sure it is connected to GitHub.

[**See detailed planning**](documentations/project_plan.md)

Total: 3 days

## Design (Project Architecture):

### Development:
**Our project was developed using Django in a Docker container.**
![Project Overview Diagram](/documentations/screenshots/django-project.png)

#### Diagram Relationships:
- Our project is **containerised** using Docker for efficient development, consistent deployment, and isolated runtime environments.  
- The Docker setup encapsulates the entire Django project, including all dependencies, ensuring that the application runs uniformly across multiple platforms.  
- The container configuration streamlines our CI/CD process, making it easier to build, test, and deploy updates in a controlled environment.  
- [Docker Compose](/docker-compose.yml) is used to orchestrate multi-container setups, allowing seamless integration with additional services such as databases (postgres).
- **Django project** is our project that is an **aggregation** of mutiple modular Django 'apps'.
    - 'accounts' app is responsible for user authentication - [click here](/myclean/accounts/) for more iformation.
    - 'service_provider' app is responsible for anything relating to the service provider in our software  - [click here](/myclean/service_provider/) for more iformation.
    - 'cleaning_services' app is responsible for listing all of the cleaning services in our software  - [click here](/myclean/cleaning_services/) for more iformation.
    - 'myclean' app is the main application responsible for the project settings.
- Django integrates seamlessly with PostgreSQL by using its built-in database engine. Key benefits include:
    - Direct support for advanced PostgreSQL features such as JSONField, ArrayField, and full-text search.
    - A robust ORM that transforms Python models into database tables and leverages efficient query generation.
    - Simplified database migrations using Django's migration tools, ensuring smooth schema updates.
    - Secure and scalable connections, making it easier to manage data integrity and performance.

[Click Here for Detailed Application Architecture](/documentations/architecture.md)

### Deployment
![Deployment Diagram](/documentations/screenshots/deployment-ase.png)

#### Cloud Service:
- Our software is deployed in a Microsoft Azure Virtual Machine:
    - Operating system: Linux
    - Size: Standard B1s (1 vcpu, 1 GiB memory)

## Iteration 1 [duration 3 weeks]
### [Detailed Iteration 1 Document](./documentations/iteration_1.md)
1. [(Service Provider) I need to be able to register my service/s so a potential client can find us.](documentations/user_stories/iter1_us_01_sp_register.md)
    - Title: **Service provider register**
    - Priority: 10
    - Estimation: 1 day (5 hours)

2. [(Client) I need to be able to see a list of service/s so I can decide on which one to contact.](documentations/user_stories/iter1_us_02_client_list_of_services.md)
    - Title: **List of services**
    - Priority: 10
    - Estimation: 3 days (15 hours)

3. [(Service Provider) I need to be able to add to my profile such as my general location and service description.](documentations/user_stories/iter1_us_03_sp_create_profile.md)
    - Title: **Service provider create profile**
    - Priority: 10
    - Estimation: 2 days (10 hours)

4. [(Service Provider) I need to be able to login to my account after registering.](documentations/user_stories/iter1_us_04_sp_login.md)
    - Title: **Service provider login**
    - Priority: 10
    - Estimation: 1 day (5 hours)

5. [(Service provider) I need to be able to logout of my account after registering/loging in.](documentations/user_stories/iter1_us_05_sp_logout.md)
    - Title: **Service provider logout**
    - Priority: 10
    - Estimation: 1 day (5 hours)

Total: 8 days / 35 hours of our budget.


## Iteration 2 [duration 3 weeks]
### [Detailed Iteration 2 Document](./documentations/iteration_2.md)
1. [(Client) I need to be able to filter services by category so I can find relevant options faster.](documentations/user_stories/iter2_us_06_client_filter_cat.md)
    - Title: **Client filter by category**
    - Priority: 10
    - Estimation: 3 days (15 hours)

2. [(Service Provider) I need to be able to view and list my availability on a schedule so clients know when I am free.](documentations/user_stories/iter2_us_07_sp_availability_schedule.md)
    - Title: **Service provider schedule**
    - Priority: 20
    - Estimation: 5 days (25 hours)

3. [(Client) I need to be able to book a cleaning service so I can schedule an appointment.](documentations/user_stories/iter2_us_08_client_book_service.md)
    - Title: **Service Provider Profile Creation**
    - Priority: 25
    - Estimation: 2 days (10 hours)

Total: 10 days / 50 hours of our budget

## Tests:
Our project includes a comprehensive suite of automated tests to ensure each component operates as intended. Here’s a brief overview of the testing strategy for each major app:

- **Cleaning Services:**  
  The tests verify that:
  - The cleaning services view is accessible.
  - The correct template is used.
  - The view’s context includes all required data (i.e., service providers and filtering categories).
  - Category filtering works correctly, including handling nonexistent categories.

  [View detailed tests and documentation in the Cleaning Services directory](/myclean/cleaning_services/)

- **Accounts:**  
  The tests cover:
  - GET requests for the login and registration views.
  - Successful registration via POST requests.
  - Correct logout redirection.

  [View detailed tests and documentation in the Accounts directory](/myclean/accounts/)

- **Service Provider:**  
  The tests include:
  - Verifying that the service provider dashboard requires authentication.
  - Testing profile update functionalities (both GET and POST requests) and ensuring changes are saved.
  - Checking the availability views (adding, viewing, and deleting availability slots).
  - Validating booking processes, including preventing double bookings.

  [View detailed tests and documentation in the Service Provider directory](/myclean/service_provider/)

Each app’s directory has a detailed README that describes its test cases further, so please refer to those for an in-depth look at our testing approach.


## Not enough time/developers:
9. [Service Provider View Bookings](documentations/user_stories/iter3_us_09_sp_view_bookings.md)  
    - Title: **Service Provider View Bookings**  
    - Priority: 30  
    - Estimation: 2 days

10. [Service Provider Update Bookings](documentations/user_stories/iter3_us_10_sp_update_bookings.md)  
    - Title: **Service Provider Update Bookings**  
    - Priority: 30  
    - Estimation: 2 days

11. [Service Provider Delete Bookings](documentations/user_stories/iter3_us_11_sp_delete_bookings.md)  
    - Title: **Service Provider Delete Bookings**  
    - Priority: 30  
    - Estimation: 2 days

12. [Search Function](documentations/user_stories/iter3_us_12_client_search.md)  
    - Title: **Search Function**  
    - Priority: 35  
    - Estimation: 3 days

13. [Service Provider Delete Profile](documentations/user_stories/iter3_us_13_sp_delete_profile.md)  
    - Title: **Service Provider Delete Profile**  
    - Priority: 40  
    - Estimation: 1 day

14. [Client Create Profile](documentations/user_stories/iter3_us_14_client_create_profile.md)  
    - Title: **Client Create Profile**  
    - Priority: 45  
    - Estimation: 2 days

15. [Direct Client-To-Provider Contact](documentations/user_stories/iter3_us_15_direct_client_to_provider_contact.md)  
    - Title: **Direct Client-To-Provider Contact**  
    - Priority: 45  
    - Estimation: 5 days

16. [Service Provider Verification Status](documentations/user_stories/iter3_us_16_verification_status.md)  
    - Title: **Service Provider Verification Status**  
    - Priority: 50  
    - Estimation: 4 days

17. [One Time Payment Front Page Advertisement](documentations/user_stories/iter3_us_17_one_time_payment.md)  
    - Title: **One Time Payment Front Page Advertisement**  
    - Priority: 50  
    - Estimation: 3 days

Total: 24 days




