from django.urls import path
from .views import leaderboard, workingLeaderboard

urlpatterns = [
    # Defines and names the url that displays the leaderboard.
    path('', leaderboard, name='leaderboard'),
    path('working', workingLeaderboard, name='workingLweaderboard'),
]
