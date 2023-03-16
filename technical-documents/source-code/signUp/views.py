from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth import get_user_model
from django.utils.encoding import force_bytes, force_str
from . import forms
from accounts.models import CustomUser
from django.contrib import messages


from .tokens import account_activation_token


def activate(request, uidb64, token):
    # User = CustomUser.objects.get

    try:
        uid = force_str(urlsafe_base64_encode(uidb64))
        user = CustomUser.objects.get(pk=id)
        user.is_user = True
        user.save()

    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_user = True
        user.save()

    return redirect('login')


def activateEmail(request, user, to_email):
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
    """
    if request.method == "POST":

        form = forms.SignUpForm(request.POST)

        # If the data entered into the form is valid save the details and
        # create a new user, otherwise throw the relevant error message
        if form.is_valid():
            user = form.save(commit=False)
            user.is_user = False
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))
            return redirect('leaderboard')
        # else:
            # messages.info(request, 'Invalid registration details')
    else:
        # GET request case
        form = forms.SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})
