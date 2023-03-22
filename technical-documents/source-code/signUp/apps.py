""" Outlines the apps for configuring user accounts via the signup page. """
from django.apps import AppConfig

class AccountsConfig(AppConfig):
    """ Configures accounts via the signup page. """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'signUp'
