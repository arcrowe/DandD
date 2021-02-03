from django.urls import path
from . import views
from home.dash_apps.finished_apps import simpleexample  # Don't delete - wont work without it!!!
urlpatterns = [
    path('', views.home, name='home')
]
