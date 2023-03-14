from django.urls import path
from .views import leaderboard, workingLeaderboard

""" Defines and names the url that displays the leaderboard.  """
urlpatterns = [
    path('', workingLeaderboard, name='leaderboard'),
    path('UI', leaderboard, name='workingLweaderboard'),
]
