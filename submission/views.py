from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # Need to make sure user is always logged in
    return HttpResponse("Hello, world. You're at the submission index.")
