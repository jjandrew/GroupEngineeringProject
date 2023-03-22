""" Outlines the app used for configuring the login app. """
from django.apps import AppConfig

class LoginConfig(AppConfig):
    """ Configures the login project.
    
    Args:
        AppConfig: The defualt Django AppConfig object for configuring an
            application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'loginApp'
