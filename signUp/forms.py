from django import forms
from accounts.models import CustomUser
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
        self.fields['first_name'].widget.attrs.update({
            'class': 'un',
            'type': 'text',
            'align': "center",
            'name': 'first_name',
            'placeholder': 'Name',
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'un',
            'type': 'text',
            'align': "center",
            'name': 'last_name',
            'placeholder': 'Surname',
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
    first_name = forms.CharField(max_length=20, label=False)
    last_name = forms.CharField(max_length=20, label=False)
    email = forms.EmailField(max_length=100)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2',)
