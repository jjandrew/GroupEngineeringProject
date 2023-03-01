from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm


def signup(request):

    form = SignUpForm(request.POST)
    context = {'form': form}

    if form.is_valid():
        # If the data in the form is validated all the inputs are stored and a new
        # user is created
        user = form.save()

        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('login')

    else:
        return render(request, 'registration/signup.html', context)
