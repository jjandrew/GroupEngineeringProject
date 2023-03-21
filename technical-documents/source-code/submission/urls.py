""" Outlines the paths to each of the URLs for the submission app. """
from django.urls import path
from submission import views


urlpatterns = [
    # Defines the URL pattern for the submission page
    path('', views.working_submission_view, name='submission'),
    path('UI', views.submission_view, name='workingSubmission'),
]
