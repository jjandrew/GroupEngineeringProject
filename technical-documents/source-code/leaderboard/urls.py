""" Defines and names the url that displays the leaderboard. """
from django.urls import path
from leaderboard.views import leaderboard


urlpatterns = [
    # Defines and names the url that displays the leaderboard.
    path('', leaderboard, name='leaderboard'),
]
