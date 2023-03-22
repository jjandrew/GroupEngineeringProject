""" Outlnies the methods to be used for the signUp app. """
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import Group
from accounts.models import CustomUser
from signUp import forms
from signUp.tokens import account_activation_token


def activate(request, uidb64, token):
    """ Activates a new user account with their id being their primary key.

    Args:
        request: The HTTP request submitted by the user.

        uidb64: A unique ID for the user's email.

        token: A object to help identify the user.

    Returns:
        redirect: 'login': Redirects the user to the login page once their,
            accounts has been validated.
    """
    # User = CustomUser.objects.get

    try:
        user = CustomUser.objects.get(pk=id)
        user.is_user = True
        user.save()

    except:
        user = None

    # If the user exists and has a valid token, save the account
    if user is not None and account_activation_token.check_token(user, token):
        user.is_user = True
        user.save()

    return redirect('login')


def activate_email(request, user, to_email) -> None:
    """ Formulates the message that gets sent in the activation email and
    sends the email to the user.

    Args:
        request: The HTTP request submitted by the user.

        user: user: The user object representing the user who is having their
            email validated.

        to_email: (str): The user's email, given as a string for ease of
            processing.
    """
    mail_subject = "Activate your user account"

    # Converts the message to be sent to the user into a string
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
        render: Signup page is shown to the user if they enter the wrong
            details.

        redirect: (leaderboard): The user is redirected to the leaderboard
            page if they have submitted a valid form.
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

    else:
        # GET request case
        form = forms.SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})
