""" Creates the class for configuring user accounts. """
from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """ Specifies the base fields to be used when configuring user accounts.

    Args:
        AppConfig (AppConfig): The AppConfig account object to be set.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
