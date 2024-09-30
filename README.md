How start up a django project

1. Create a normal python project
2. "pip install django"       # To install django
3. "django-admin startproject mysite ."   # Create project mysite with directory
4. "python manage.py startapp job_application" # Create app (can be multiple)
5. In mysite/settings.py add app to INSTALLED_APPS (e.g. job_application)
6. "python manage.py runserver"     # To run the app
