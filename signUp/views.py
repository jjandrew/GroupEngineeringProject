from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.contrib import messages

def signup(request):
    if request.method == "POST":

        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_valid = False
            user.save()
            return redirect('login')
        else:
            messages.info(request, 'invalid registration details')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


