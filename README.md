# Login System with Python and Django

This is a guide on setting up a login system using Python and Django. Follow the steps below to get started.

## Setup Steps on the Command Line

1. Install virtualenv by running the command: `pip install virtualenv`.
2. Create a virtual environment by executing: `virtualenv venv`.
3. Activate the virtual environment using: `venv\Scripts\activate`.
4. Install Django by running: `pip install django`.
5. Open the project directory in your preferred code editor by executing: `code .`.

## Steps to Start the Django Project Inside the Virtual Environment

1. Create a Django project using the command: `django-admin startproject login_system`.
2. Create a Django app by running: `python manage.py startapp login_app`.
3. In the [urls.py](login_system/urls.py) file, add the following line: `path('', include('login_app.urls'))`.

4. Create a new [urls.py](login_app/urls.py) file inside the `login_app` folder.

5. To run the server, type the command: `python manage.py runserver`.

## How the Django Project Works

1. When you run the Django project, it first checks the settings of the app in the [settings.py](login_system/settings.py) file.

2. Then, it goes to the [urls.py](login_system/urls.py) file, where the URLs for our app (in this case, `login_app`) are defined.

3. Next, it looks for the URL defined in the [urls.py](login_app/urls.py) file of the app.

4. The corresponding function defined in [urls.py](login_app/urls.py) is executed, which returns an HttpResponse.
