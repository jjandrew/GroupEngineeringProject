from django.shortcuts import render, redirect
from loginApp.models import User


def leaderboard(request):
    leaderboard_data = User.objects.order_by('-points')
    return render(request, 'leaderboard/leaderboard.html', {'leaderboard': leaderboard_data})


def add_to_leaderboard(request):
    if request.method == 'POST':
        player_name = request.POST.get('player_name')
        score = request.POST.get('score')
        leaderboard_entry = User(username=player_name, points=score)
        leaderboard_entry.save()
        return redirect('leaderboard')
    else:
        return render(request, 'leaderboard/add_to_leaderboard.html')
