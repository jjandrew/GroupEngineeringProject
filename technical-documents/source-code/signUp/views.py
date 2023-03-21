""" Outlines the methods to be used in the signUp app. """
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from accounts.models import CustomUser
from django.contrib.auth.models import Group
from signUp import forms
from signUp.tokens import account_activation_token


def activate(token):  # request, uidb64,
    """ Gives points for each day since a building has been checked

    Args:
        token (str): The name of the building to calculate points for
            provided as a string for readability.

    Returns:
        redirect: redirects the user to the login page.
    """
    # User = CustomUser.objects.get

    try:
        # uid = force_str(urlsafe_base64_encode(uidb64))
        user = CustomUser.objects.get(pk=id)
        user.is_user = True
        user.save()

    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_user = True
        user.save()

    return redirect('login')


def activate_email(request, user, to_email) -> None:
    """ Sends the user an email to validate their email address.

    Args:
        request : The HTTP request (page) submitted by the user.
        user (user): The user object of the user who's email address
            is being validated.
        to_email : The email address being validated.
    """
    mail_subject = "Activate your user account"

    message = render_to_string(
        "signUp/template_activate_user.html",
        {"user": user.username,
         "domain": get_current_site(request).domain,
         "uid": urlsafe_base64_encode(force_bytes(user.pk)),
         "token": account_activation_token.make_token(user),
         "protocol": 'https' if request.is_secure() else "http"
         }
    )
    email = EmailMessage(mail_subject, message, to=[to_email])
    email.send()


def signup(request):
    """ Displays the sign up page (GET request) and takes the data from the
    sign up form, validates it and creates a new user, displaying any error
    messages if necessary.

    Args:
        request (str): The HTTP request (page) submitted by the user.

    Returns:
        redirect: redirects the user to either the leaderboard (are signed in)
        or the signup page (don't have an account).
    """
    if request.method == "POST":

        form = forms.SignUpForm(request.POST)

        # If the data entered into the form is valid save the details and
        # create a new user, otherwise throw the relevant error message
        if form.is_valid():
            user = form.save(commit=False)
            user.is_user = False
            user.save()
            user_group = Group.objects.get(name='user')
            user_group.user_set.add(user)
            activate_email(request, user, form.cleaned_data.get('email'))
            return redirect('leaderboard')
        # else:
            # messages.info(request, 'Invalid registration details')
    else:
        # GET request case
        form = forms.SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})
