""" Outlines the URLs to be used by the homepage. """
from django.urls import path
from homepage import views

# The URL pattern for the homepage.
urlpatterns = [
    path('', views.index, name='homepage'),
]
