from django.urls import path
from .views import leaderboard, add_to_leaderboard

urlpatterns = [
    path('', leaderboard, name='leaderboard'),
    path('add-to-leaderboard/', add_to_leaderboard, name='add_to_leaderboard'),
]
