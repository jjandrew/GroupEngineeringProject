"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Adds a project level url for the sign up page
    path('accounts/', include("signUp.urls")),

    # Adds a path to all the views provided by the auth app
    path('accounts/', include("django.contrib.auth.urls")),

    # Adds a project level url for the logins
    path('login/', include('loginApp.urls')),

    # Takes the user to the location page if they are logged in
    path('location/', include("location.urls")),

    # The leaderboard url
    path('leaderboard/', include('leaderboard.urls')),

    # Takes the user to the 'homepage' if they are not logged in
    path('', TemplateView.as_view(
        template_name='home.html'), name='homepage'),

    # Path for logging out the user
    path('logout/', views.userLogout, name='logout'),

    # Path for submission
    path('submission/', include('submission.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
