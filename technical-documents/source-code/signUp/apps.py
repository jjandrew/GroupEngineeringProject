""" Creates the class for configuring accounts. """
from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """ Specifies the base fields to be used when configuring user accounts.

    Args:
        AppConfig (AppConfig): The AppConfig signUp object to be set.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'signUp'
