""" Outlines the apps used for configuring the submission. """
from django.apps import AppConfig


class SubmissionConfig(AppConfig):
    """ Outlines the fields for configuring the submission page.

    Args:
        AppConfig: (AppConfig): The django configuration object for configuring
            the submission page.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'submission'
