How start up a django project

1. Create a normal python project
2. Create .gitignore with all excluded files and folders and commit/push
3. "pip install django"       # To install django
4. "django-admin startproject mysite ."   # Create project mysite with directory
5. "python manage.py startapp job_application" # Create app (can be multiple)
6. In mysite/settings.py add app to INSTALLED_APPS (e.g. job_application)
7. "python manage.py runserver"     # To run the app
8. "class "Form(models.Model):" # in models.py set structure of database
9. Add __str__ method for string representation
10. "python manage.py makemigrations"  # generate python code for db in 0001_initial.py
11. "python manage.py migrate  # apply structure to create tables in db
12. Create templates directory for html files with index.html in it
13. In j_a views file create functions to handle requests
14. In j_a create urls.py with urlpatterns, add path 'index'
15. in mysite urls.py include the urls from the app, j_a and other apps


