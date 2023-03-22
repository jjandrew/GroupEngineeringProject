""" Outlines the apps used for configuring the game keeper homepage. """
from django.apps import AppConfig


class GkhomepageConfig(AppConfig):
    """ Outlines the fields for configuring the game keeper homepage.

    Args:
        AppConfig: (AppConfig): The django configuration object for configuring
            the submission page.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gkHomepage'
