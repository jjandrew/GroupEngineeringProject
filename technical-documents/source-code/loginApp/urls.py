""" Specfies the URLs used by the login part of the project. """
from django.contrib import admin
from django.urls import path
from loginApp import views

urlpatterns = [
    # Path for the admin URL
    path("admin/", admin.site.urls),
    # Path for the login URL
    path('', views.login_user, name="login"),
]
