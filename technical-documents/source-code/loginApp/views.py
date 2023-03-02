from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import LoginForm
from django.http import HttpResponseRedirect

def login_user(request):
    """ Displays the login form and takes the data entered into it and 
    authenticates the user, redirecting them onto the main page or keeping
    them at the login page.
    """

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        # If the user exists and is valid, they are logged in and redirected
        # to the homepage
        if user is not None:
            login(request, user)
            print("here")
            return redirect('/')
        else:
            # Otherwise, an error is thrown and they're returned to the login
            messages.error(request, ("Username or password is incorrect!"))
            return redirect('login')

    else:
        # In the case the form being requested as a GET request,
        # the login form is displayed.
        return render(request, 'registration/login.html', {})


def userLogout(request):
    """ Uses the built in Django view to logout the user and redirect them
    to the login page.
    """
    logout(request)
    return redirect('homepage')
