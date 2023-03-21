""" Outlines the fields and data to be displayed to the user in the login
page.
"""
from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    """ Defines the parameters and data collected from the login form,
    in addition to methods for cleaning and validating the data.

    Args:
        forms.Form: Form: The login form to be displayed to
            and received from, the user.
    """
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        """ 'Cleans' the username and password values collected from the login
        page. Also performs validation, preventing invalid logins.

        Returns:
            cleaned_data: 'Cleaned' versions of the data the user entered into
                the login form, doing this ensures it is valid and able to be
                parsed.
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
            request: The HTTP request, which the user submits when loging in.

        Returns:
            User: user: The user object corresponding to the user that just
            logged in.
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
