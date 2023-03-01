from django.urls import path
from . import views

urlpatterns = [
    # Defines the URL pattern for the submission page
    path('', views.submission_view, name='submission'),
]
