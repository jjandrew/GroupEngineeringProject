""" Outlines the URLs that are used as part of the signup app. """
from django.urls import path
from signUp import views

urlpatterns = [
    # Declares the pattern for the sign up page
    path('signup/', views.signup, name="signup"),
    path('activate/<uidb64>/<token>', views.activate, name='activate')
]
