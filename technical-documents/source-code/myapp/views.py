""" Outlines the methods to be used in the main app. """
from django.shortcuts import render, redirect
from django.contrib.auth import logout


def user_logout(request):
    """ Uses the built in Django view to logout the user and redirect them
    to the login page.

    Args:
        request: The HTTP request sent by the user.

    Returns:
        redirect(): When logged out, the user is redirected to the login page,
        as no other parts of the webpage can/should be accessed if the user
        isn't logged in.
    """
    logout(request)
    return redirect('/login')


def privacy_policy(request):
    """ Displays the privacy policy page for the user

    Args:
        request: The HTTP request sent by the user.

    Returns:
        render(): Returns the privacy policy webpage.
    """
    return render(request, 'privacypolicy/privacypolicy.html')
