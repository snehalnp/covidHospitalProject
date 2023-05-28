# COVID-19 Hospital API

This project provides an API for managing COVID-19 patients and doctors in a hospital.

## Requirements
- Python 3.x
- Django
- MySQL

1) Create a virtual environment (optional but recommended):

py -m venv env_name
env_name\Scripts\activate.bat

2) Install the dependencies: 

Django, mysqlclient, django rest framework

3) Create Django Project:

django-admin startproject project_name
cd project_name

4) Create Django App:

django-admin startapp app_name
OR
python manage.py app_name

Add the app_name in 'INSTALLED_APPS' in settings.py

5) Add all the installed dependencies to a file:

pip freeze > requirements.txt

6)Configure the Database:

Update the `DATABASES` settings with your MySQL database credentials

7) Create models as per the requirement in models.py then run following commands:

python manage.py makemigrations
python manage.py migrate

8) Add all the URLS with respect to your views.py (used for business logic) and models.py

9) Start development server:

python manage.py runserver
