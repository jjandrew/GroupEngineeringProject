""" Outlines the URLs to be used by the gamekeeper homepage. """
from django.urls import path
from gkHomepage import views

# The URL patters for this section
urlpatterns = [
    path('', views.index, name='gkHomepage'),
]
