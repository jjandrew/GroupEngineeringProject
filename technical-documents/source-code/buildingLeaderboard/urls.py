from django.urls import path
from .views import buildingLeaderboard

""" Defines and names the url that displays the leaderboard.  """
urlpatterns = [
    # Defines and names the url that displays the leaderboard.
    path('', buildingLeaderboard, name='buildingLeaderboard'),
]
