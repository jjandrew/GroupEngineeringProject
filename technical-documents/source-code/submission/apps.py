""" Creates the class for configuring submission models. """
from django.apps import AppConfig


class SubmissionConfig(AppConfig):
    """ Specifies the base fields to be used when configuring submission
    models.

    Args:
        AppConfig (AppConfig): The AppConfig submission object to be set.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'submission'
