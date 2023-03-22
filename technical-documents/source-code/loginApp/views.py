""" Outlines the methods to be used for the login section of the project. """
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


def login_user(request):
    """ Displays the login form and takes the data entered into it and
    authenticates the user, redirecting them onto the main page or keeping
    them at the login page.

    Args:
        request: The HTTP request submitted by the user.

    Return:
        redirect(/gkhomepage): Redirects the user to the gamekeeper homepage
            if they entered correct login details and are a valid gamekeeper.

        redirect(/): Redirects the user to the homepage if they successfully
            login and aren't a game keeper.

        redirect(login): Redirects the user to the login page if they entered
            incorrect data into the form.

        render: If the login page is being requested as a get request, the
            user is presented with the login page.
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

    Request:
        redirect:('homepage'): Redirects the user to the homepage if they log
            out.
    """
    logout(request)
    return redirect('homepage')
