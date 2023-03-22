from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse

def userLogout(request):
    """ Uses the built in Django view to logout the user and redirect them
    to the login page.
    """
    logout(request)
    return redirect('/login')


def privacyPolicy(request):
    """ Displays the privacy policy page for the user """
    return render(request, 'privacypolicy/privacypolicy.html', {})


def index(request):
    """ Displays a welcome message if the user is at the home page. """
    return HttpResponse("Hello, world. You're at the home page.")
