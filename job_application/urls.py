from django.urls import path
from . import views

urlpatterns = [
    # The name attribute allows referring to this URL pattern using 'index' in
    # templates and views
    path('', views.index, name='index'),
]
