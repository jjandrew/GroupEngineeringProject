from django.shortcuts import render
from accounts.models import CustomUser

# Create your views here.
def index(request):
    print("____",request.user.points)
    username = request.user.username
    email = request.user.email
    points = request.user.points
    streak = request.user.streak


    args = {'username': username, 'email': email, 'points': points, 'streak': streak}
    return render(request, "myprofile/myprofile.html",args)