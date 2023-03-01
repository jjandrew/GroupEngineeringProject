from django.urls import path
from . import views

urlpatterns = [
   # Defines and names the url that displays the leaderboard.
   path('', views.home, name="location"),
]