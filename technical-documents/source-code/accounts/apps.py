""" Outlines the apps used for configuring the accounts. """
from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """ Outlines the fields for configuring the accounts page.

    Args:
        AppConfig: (AppConfig): The django configuration object for configuring
            the submission page.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
