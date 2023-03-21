""" Creates the class for the outlining the data stored for admins """
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import CustomUser


class CustomUserAdmin(UserAdmin):
    """ Specifies the the sets of fields stored for every admin user,
    along with a list of which user metrics are displayed for them.

    Args:
        UserAdmin (UserAdmin): The object corresponding to the current admin
            user.
    """
    # The fields that are displayed for the admin user
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'points'
        )

    # The base data fields that are stored for admin users
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('points', None)
        })
    )

    # Additional data fields that can be stored on admin users
    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ( 'is_user', 'points')
        })
    )


admin.site.register(CustomUser, CustomUserAdmin)
