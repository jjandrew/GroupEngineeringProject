from django.shortcuts import redirect,render
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import LoginForm
from django.http import HttpResponseRedirect

# Create your views here.
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)

        # More user verification required??
        if user is not None:
            login(request,user)
            return redirect('/')

        else:
            messages.success(request, ("There was an error logging in"))
            return redirect('login')

    else:
        return render(request, 'registration/login.html', {})



def userLogout(request):
    """ Uses the built in logout view to logout a user"""
    logout(request)
    return redirect('')