""" Creates the class for configuring leaderboard models. """
from django.apps import AppConfig


class LeaderboardConfig(AppConfig):
    """ Specifies the base fields to be used when configuring leaderboard
    models.

    Args:
        AppConfig (AppConfig): The AppConfig submission object to be set.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'leaderboard'
