from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.contrib import messages

def signup(request):
    """ Displays the sign up page (GET request) and takes the data from the
    sign up form, validates it and creates a new user, displaying any error
    messages if necessary.
    """
    if request.method == "POST":

        form = SignUpForm(request.POST)

        # If the data entered into the form is valid save the details and
        # create a new user, otherwise throw the relevant error message
        if form.is_valid():
            user = form.save(commit=False)
            user.is_valid = False
            user.save()
            return redirect('login')
        #else:
            #messages.info(request, 'Invalid registration details')
    else:
        # GET request case
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})
