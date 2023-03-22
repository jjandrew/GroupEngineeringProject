""" Outlines the app for configuring the gamekeeper sign up. """
from django.apps import AppConfig


class GksignupConfig(AppConfig):
    """ Configures gamekeeper accounts via the GKSignUp page. """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gkSignUp'
