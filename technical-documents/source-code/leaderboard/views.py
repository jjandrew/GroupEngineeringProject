from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser


@login_required
def leaderboard(request):
    """ A function for displaying and ordering (in descending order) the
    leaderboard. Note, to access this, the user must be logged in.
    """
    leaderboard = CustomUser.objects.filter(
        points__gt=0).order_by('-points')
    try:
        first = leaderboard[0]
        second = leaderboard[1]
        third = leaderboard[2]
        remaining = leaderboard[3:]
        return render(request, 'UI/leaderboard.html', {'first': first, 'second': second, 'third': third, 'remaining': remaining})
    except IndexError:
        try:
            return render(request, 'UI/leaderboard.html', {'first': first, 'second': second, 'third': third, 'remaining': []})
        except UnboundLocalError:
            try:
                third = {
                    'username': "Insufficient Users",
                    'points': 0
                }
                return render(request, 'UI/leaderboard.html', {'first': first, 'second': second, 'third': third, 'remaining': []})
            except UnboundLocalError:
                try:
                    second = {
                        'username': "Insufficient Users",
                        'points': 0
                    }
                    return render(request, 'UI/leaderboard.html', {'first': first, 'second': "Insufficient Players",
                                                                   'third': "Insufficient Players", 'remaining': []})
                except UnboundLocalError:
                    first = {
                        'username': "Insufficient Users",
                        'points': 0
                    }
                    return render(request, 'UI/leaderboard.html', {'first': "Insufficient Players", 'second': "Insufficient Players",
                                                                   'third': "Insufficient Players", 'remaining': []})
