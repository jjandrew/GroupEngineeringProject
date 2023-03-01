from django import forms
from accounts.models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

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
            'placeholder': 'Email@Exeter.ac.uk',
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

    def clean_email(self):
        """Validates the email the user enters into the sign up form to ensure it is
        a valid @exeter.ac.uk email"""
        cleanEmail = self.cleaned_data['email']
        if "@exeter.ac.uk" not in cleanEmail:
            raise forms.ValidationError("Must be an Exeter University email (...@exeter.ac.uk)")

        return cleanEmail

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password1']
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError("Passwords do not match")
        return password2


    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = CustomUser.objects.exclude(pk=self.instance.pk).get(username=username)
        except CustomUser.DoesNotExist:
            return username
        raise forms.ValidationError(u'Username "%s" is already in use.' % username)




    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2',)
