from django.shortcuts import redirect,render
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.


def login_user(request):
    return render(request, 'authenticate/login.html', {})