""" Outlines the paths to each of the URLs for the login app. """
from django.contrib import admin
from django.urls import path
from dashboard import views


urlpatterns = [
    # Path for the admin URL
    path("admin/", admin.site.urls),
    # Path for the login URL
    path('dashboard/', views.dashboard, name="dashboard"),
]
