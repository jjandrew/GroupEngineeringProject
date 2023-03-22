""" Oulines the functions to be used by the main part of the app. """
from django.shortcuts import render, redirect
from django.contrib.auth import logout


def user_logout(request):
    """ Uses the built in Django view to logout the user and redirect them
    to the login page.

    Args:
        request: The HTTP request submitted by the user.

    Returns:
        redirect: (login): Redirects the user to the login page if they log
            themselves out.
    """
    logout(request)
    return redirect('/login')


def privacy_policy(request):
    """ Displays the privacy policy page for the user

    Args:
        request: The HTTP request submitted by the user.

    Returns:
        render(privacypolicy): Displays the privacy policy webpage.
    """
    return render(request, 'privacypolicy/privacypolicy.html', {})
