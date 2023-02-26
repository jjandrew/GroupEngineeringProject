from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class UserSignUpView(generic.CreateView):
    """A class that defines a view for user registration using generic templates"""
    form_class = UserCreationForm

    # Redirects the user to the login page once they sign up MAY THROW ERROR AS INCORRECT FILE PATH USED.
    success_url = reverse_lazy("login")
    template_name = "signup/signup.html"
