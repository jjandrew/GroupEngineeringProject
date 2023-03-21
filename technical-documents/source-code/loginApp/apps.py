""" Creates the class for logging in accounts. """
from django.apps import AppConfig


class LoginConfig(AppConfig):
    """ Specifies the base fields to be used when logging in accounts.

    Args:
        AppConfig (AppConfig): The AppConfig signUp object to be set.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'loginApp'
