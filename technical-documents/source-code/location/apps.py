""" Creates the class for configuring the location app. """
from django.apps import AppConfig


class UserLocationConfig(AppConfig):
    """ Specifies the base fields to be used when configuring the location
    app.

    Args:
        AppConfig (AppConfig): The AppConfig signUp object to be set.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'location'
