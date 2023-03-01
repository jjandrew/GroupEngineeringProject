from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    # Path for the admin URL
    path("admin/", admin.site.urls),
    # Path for the login URL
    path('', views.login_user, name="login"),
]
