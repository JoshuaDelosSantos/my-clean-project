# Static Directory (Project)

## Overview
The **Static** directory contains all the static files for the MyClean project. These files include CSS, JavaScript, images, and other assets that are used across the application.

## Structure
The static directory is organised as follows:

### css/
This directory contains all the CSS files used for styling the application. The main stylesheet is `style.css`.

### images/
This directory contains all the image files used in the application, such as logos, icons, and other graphics.

## Usage
To use the static files in your Django templates, you need to load the static template tag and reference the files using the `{% static %}` tag.

### Example (base.html)
```
{% load static %}
<html>

  <head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <title>
      {% block title%}
        My Clean
      {% endblock %}
    </title>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
  </head>

  <body>

    <nav>
        <div class="nav-links-container">
            <a href="{% url 'home' %}">Home</a>
            <a href="{% url 'login_sp' %}">Login</a>
            <a href="{% url 'register_sp' %}">Register</a>
        </div>
    </nav>

    <!-- We can inject any html code into the 'block content!' -->
    {% block content%} 

    {% endblock %}
  </body>

</html>

```