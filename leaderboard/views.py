from django.shortcuts import render, redirect
from loginApp.models import User
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser


@login_required
def leaderboard(request):
    leaderboard = CustomUser.objects.order_by('-points')
    return render(request, 'leaderboard/leaderboard.html', {'leaderboard': leaderboard})
