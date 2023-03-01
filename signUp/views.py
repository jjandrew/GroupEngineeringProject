from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from loginApp.models import User


def signup(request):

    form = SignUpForm(request.POST)
    context = {'form': form}

    if form.is_valid():
        # If the data in the form is validated all the inputs are stored and a new
        # user is created
        form.save()
        email = form.cleaned_data.get('email')
        username = form.cleaned_data.get('username')
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        password = form.cleaned_data.get('password')
        new_user = User(username=username, email=email,
                        first_name=first_name, last_name=last_name, points=0)
        new_user.save()
        user = form.save()

        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('login')

    else:
        return render(request, 'registration/signup.html', context)
