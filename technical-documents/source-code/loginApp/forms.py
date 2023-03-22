""" Outlines the structure and content of the login forms to be displayed to
the user.
"""
from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    """ Defines the parameters and data collected from the login form,
    in addition to methods for cleaning and validating the data.

    Args:
        forms.Form: (Form): The built in Django form object that is going to
            be altered into the login form.
    """
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        """ 'Cleans' the username and password values collected from the login
        page. Also performs validation, preventing invalid logins.

        Returns:
            str: cleaned_data: 'Cleaned' version of the data the user has
                entered into the login form.
        """
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        # Prevents users that are already logged in or don't exist from logging in.
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        """ Authenticates and returns the user object entered into the login
        form.

        Args:
            request: The HTTP request submitted by the user.

        Returns:
            user: The user object corresponding to the user who is trying to
                login.
        """
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user

    def __init__(self, *args, **kwargs):
        """ The constructor for the login form, which specifies the CSS characteristics for
        both the username and password fields in the login page.
        """
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'un',
            'type': 'text',
            'align': "center",
            'name': 'username',
            'placeholder': 'Username',

        })
        self.fields['password'].widget.attrs.update({
            'class': 'pass',
            'type': 'password',
            'align': "center",
            'name': 'password',
            'placeholder': 'Password',
        })

        # username = forms.CharField(max_length=100)
        # password = forms.CharField(widget=forms.PasswordInput(render_value=False), max_length=100)
