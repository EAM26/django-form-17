How start up a django project

1. Create a normal python project
2. "pip install django"       # To install django
3. "django-admin startproject mysite ."   # Create project mysite with directory
4. "python manage.py startapp job_application" # Create app (can be multiple)
5. In mysite/settings.py add app to INSTALLED_APPS (e.g. job_application)
6. "python manage.py runserver"     # To run the app
7. "class "Form(models.Model):" # in models.py set structure of database
8. Add __str__ method for string representation
9. "python manage.py makemigrations"  # generate python code for db in 0001_initial.py
10. "python manage.py migrate  # apply structure to create tables in db
11. Create templates directory for html files with index.html in it
12. In j_a views file create functions to handle requests
13. In j_a create urls.py with urlpatterns, add path 'index'
14. in mysite urls.py include the urls from the app, j_a and other apps


