from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm


def signup(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = form.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('login')
    context = {
        'form': form
    }

    return render(request, 'registration/signup.html', context)
