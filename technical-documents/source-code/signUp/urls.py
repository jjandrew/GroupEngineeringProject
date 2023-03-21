""" Outlines the paths to each of the URLs for the signUp app. """
from django.urls import path
from signUp import views


urlpatterns = [
    # Declares the pattern for the sign up page
    path('signup/', views.signup, name="signup"),
    path('activate/<uidb64>/<token>', views.activate, name='activate')
]
