""" The URLs to be used by the submission page. """
from django.urls import path
from submission import views

urlpatterns = [
    # Defines the URL pattern for the submission page
    path('', views.working_submission_view, name='submission'),
    path('UI', views.submission_view, name='workingSubmission'),
]
