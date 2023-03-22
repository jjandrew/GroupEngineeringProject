""" Outlines the URLs to be used by the gamekeeper sign up. """
from django.urls import path
from gkSignUp import views


urlpatterns = [
    # Declares the pattern for the sign up page
    path('gkSignUp/', views.signup, name="gkSignUp"),
    path('activate/<uidb64>/<token>', views.activate, name='activate')
]
