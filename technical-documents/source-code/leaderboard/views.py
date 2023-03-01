from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser

@login_required
def leaderboard(request):
    """ A function for displaying and ordering (in descending order) the
    leaderboard. Note, to access this, the user must be logged in.
    """
    leaderboard = CustomUser.objects.filter(points__gt=0).order_by('-points')
    return render(request, 'leaderboard/leaderboard.html',
                  {'leaderboard': leaderboard})
