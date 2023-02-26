from django.shortcuts import render, redirect
from .models import Leaderboard

def leaderboard(request):
    leaderboard_data = Leaderboard.objects.order_by('-score')
    return render(request, 'leaderboard/leaderboard.html', {'leaderboard_data': leaderboard_data})

def add_to_leaderboard(request):
    if request.method == 'POST':
        player_name = request.POST.get('player_name')
        score = request.POST.get('score')
        leaderboard_entry = Leaderboard(player_name=player_name, score=score)
        leaderboard_entry.save()
        return redirect('leaderboard')
    else:
        return render(request, 'add_to_leaderboard.html')
    
