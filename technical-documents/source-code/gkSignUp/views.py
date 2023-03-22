""" Outlines the functions to be used in the gamekeeper sign up. """
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.models import Group
from accounts.models import CustomUser
from gkSignUp import forms
from gkSignUp.tokens import account_activation_token


def activate(request, uidb64, token):
    """" Activates a new user account with their id being their primary key.

    Args:
        request: The HTTP request submitted by the user.
        uidb64: A unique ID for the user's email.
        token: A object to help identify the user.

    Returns:
        redirect: 'login': Redirects the user to the login page once their,
            account has been validated.
    """
    # User = CustomUser.objects.get

    try:
        uid = force_str(urlsafe_base64_encode(uidb64))
        user = CustomUser.objects.get(pk=id)
        user.is_user = True
        user.save()

    except:
        user = None

    # If the user exists and has a valid token, they are signed in
    if user is not None and account_activation_token.check_token(user, token):
        user.is_user = True
        user.save()

    return redirect('login')


def activate_email(request, user, to_email: str) -> None:
    """ Activates the gamekeeper's email when they sign up.

    Args:
        request: The HTTP request submitted by the user.
        user: (User): The User object corresponding to the user trying to sign
            in.
        to_email: (str): The email of the user trying to sign in, as a string
            for ease of processing.
    """
    mail_subject = "Activate your user account"

    # Formats the email to sent to the user as a string
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
        request: The HTTP request submitted by the user.

    Returns:
        redirect(): If the user has filled in the form (POST request), they are
            redirected to the leaderboard.

        render(): If the signup page is being requested as a GET request, the
            sign up page is shown to the gamekeeper.
    """
    if request.method == "POST":

        form = forms.gkSignUpForm(request.POST)

        # If the data entered into the form is valid save the details and
        # create a new user, otherwise throw the relevant error message
        if form.is_valid():
            user = form.save(commit=False)
            user.is_user = False
            user.save()
            user_group = Group.objects.get(name='Gamekeeper')
            user_group.user_set.add(user)
            activate_email(request, user, form.cleaned_data.get('email'))
            return redirect('leaderboard')

    else:
        # GET request case
        form = forms.gkSignUpForm()

    return render(request, 'gkHomepage/gkSignup.html', {'form': form})
