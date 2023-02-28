from django.shortcuts import render, redirect
from loginApp.models import User
from django.contrib.auth.decorators import login_required

@login_required
def leaderboard(request):
    leaderboard = User.objects.order_by('-points')
    return render(request, 'leaderboard/leaderboard.html', {'leaderboard': leaderboard})

@login_required
def add_to_leaderboard(request):
    if request.method == 'POST':
        player_name = request.POST.get('player_name')
        score = request.POST.get('score')
        leaderboard_entry = User(username=player_name, points=score,
                                 email='test@test.com', first_name="testf", last_name="testl")
        leaderboard_entry.save()
        return redirect('leaderboard')
    else:
        return render(request, 'leaderboard/add_to_leaderboard.html')
