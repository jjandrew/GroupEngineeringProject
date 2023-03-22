""" Determines whether a user has a specific group. """
from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name:str) -> str:
    """ Checks if a user is part of a specific group or not.

    Args:
        user:(CustomUser): The CustomUser object corresponding to the user.
        group_name: The name of the group being checked, as a string.

    Returns:
        str: group: The name of group being returned as a string for ease of processing.
    """
    group =  Group.objects.get(name=group_name)
    return group in user.groups.all()
