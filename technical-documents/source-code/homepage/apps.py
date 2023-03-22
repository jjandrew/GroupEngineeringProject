""" Outlines the configurations required to configure the homepage. """
from django.apps import AppConfig


class HomepageConfig(AppConfig):
    """ Specifies the homepage configuration. """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'homepage'
