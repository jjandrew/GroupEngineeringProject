from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from loginApp.models import User


def signup(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        # email = form.cleaned_data.get('email')
        # first_name = form.cleaned_data.get('first_name')
        # last_name = form.cleaned_data.get('last_name')
        # new_user = User(username=username, email=email,
        #                 first_name=first_name, last_name=last_name, points=0)
        # new_user.save()
        # TODO just gonna guess we don't want to save the password???
        # password = form.cleaned_data.get('password')
        user = form.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('login')
    context = {
        'form': form
    }

    return render(request, 'registration/signup.html', context)
