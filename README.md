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

## Not enough time/developers: 
1. [user story title](./user_stories/user_story_01_title.md), priority XX, YY days 
2. ...

Total: YY days




