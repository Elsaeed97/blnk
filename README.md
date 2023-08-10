# Loan Management System

this is a task for a back-end developer role at blnk

# Introduction
This is Web Based Application for managing loans built with  Python, Django, Django-rest framework and Postgresql database.
And has different user roles: Loan Providers, Loan Customers, and Bank Personnel.

# Installation
git clone https://github.com/Elsaeed97/blnk.git
cd blnk/backend

### Create a virtualenv
- virtualenv venv
- source venv/bin/activate

### Install the dependencies
 pip install -r requirements.txt

### Run the Migrations
- python manage.py migrate
- python manage.py makemigrations

### Run development server
python manage.py runserver

### Run tests
python manage.py test

# Using Docker
you can use the make file provided to run commands in an easy way

### Build and Up the project
- make up-build

### Migrate
- make migrate
  
### makemigrations
- make makemigrations
  
### test
- make test

### createsuperuser
- make createsuperuser

### test 
- make test

# API Endpoints
You can find API Endpoints in the blnk-collection.json file

# API Documentaion 
YASG: http://0.0.0.0:8000/redoc/




