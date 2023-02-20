from django.shortcuts import redirect,render
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('location')

        else:
            messages.success(request, ("There was an error login in"))
            return redirect('login')

    else:
        return render(request, 'loginApp/login.html', {})