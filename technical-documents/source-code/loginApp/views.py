""" Outlines the methods to be used in the login app. """
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


def login_user(request):
    """ Displays the login form and takes the data entered into it and
    authenticates the user, redirecting them onto the main page or keeping
    them at the login page.

    Args:
        request: The HTTP request, which the user submits when loging in.

    Returns:
        redirect: (login): If the user's login is incorrect they are
            redirected to the login page to reattempt.

        redirect: (/): Sends the user to the homepage if they had a valid
            login.

        redirect: (/gkHomepage/): If the user is a gamekeeper and they had a
            correct login, they are redirected to the gamekeeper homepage.

        render: Displays the login page to the user if the request they
            submitted is a GET request.
    """

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None and user.groups.filter(name="Gamekeeper").exists():
            login(request, user)
            return redirect('/gkHomepage/')
        # If the user exists and is valid, they are logged in and redirected
        # to the homepage
        elif user is not None:
            login(request, user)
            return redirect('/')
        else:
            # Otherwise, an error is thrown and they're returned to the login
            messages.error(request, ("Username or password is incorrect!"))
            return redirect('login')

    else:
        # In the case the form being requested as a GET request,
        # the login form is displayed.
        return render(request, 'registration/login.html', {})


def user_logout(request):
    """ Uses the built in Django view to logout the user and redirect them
    to the login page.

    Args:
        request: The HTTP request submitted by the user.

    Returns:
        redirect(): Redirects the user to the homepage.
    """
    logout(request)
    return redirect('homepage')
