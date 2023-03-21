""" Outlines the paths to each of the URLs for the location app. """
from django.urls import path
from location import views


urlpatterns = [
   # Defines and names the url that displays the location page.
   path('', views.home, name="location"),
]
