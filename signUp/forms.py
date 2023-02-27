from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'un',
            'type': 'text',
            'align': "center",
            'name': 'username',
            'placeholder': 'Username',

        })
        self.fields['email'].widget.attrs.update({
            'class': 'un',
            'type': 'email',
            'align': "center",
            'name': 'email',
            'placeholder': 'Email',
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'pass',
            'type': 'password',
            'align': "center",
            'name': 'password1',
            'placeholder': 'Password',
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'pass',
            'type': 'password',
            'align': "center",
            'name': 'password2',
            'placeholder': 'Confirm password',
        })
    username = forms.CharField(max_length=20, label=False)
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)
