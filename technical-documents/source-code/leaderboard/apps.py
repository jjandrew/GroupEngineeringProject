""" Outlines the configurations required for configuring the leaderboard. """
from django.apps import AppConfig


class LeaderboardConfig(AppConfig):
    """ Outlines the fields for configuring the leaderboard.

    Args:
        AppConfig: (AppConfig): The django configuration object for configuring
            the leaderboard.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'leaderboard'
