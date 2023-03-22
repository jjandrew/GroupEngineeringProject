""" Defines and names the url that displays the leaderboard.  """
from django.urls import path
from .views import buildingLeaderboard

urlpatterns = [
    # Defines and names the url that displays the leaderboard.
    path('', buildingLeaderboard, name='buildingLeaderboard'),
]
