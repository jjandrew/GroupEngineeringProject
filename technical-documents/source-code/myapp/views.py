from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse


def userLogout(request):
    """ Uses the built in logout view to logout a user"""
    logout(request)
    return redirect('/')


def index(request):
    return HttpResponse("Hello, world. You're at the home page.")
