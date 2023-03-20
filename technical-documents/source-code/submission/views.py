from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
from .forms import ImageForm
from accounts.models import CustomUser


def addPoints(username, points):
    """ Lets the user enter points, and validates the points they enter into
    the form; to execute this function, the user must be logged in.
    """
    # Check if user already has a score entered
    if points <= 0:
        raise RuntimeError("Can't add negative points")

    # Add the points to a user's points
    user = CustomUser.objects.get(username=username)
    user.points += points
    user.save()


@login_required
def submission_view(request):
    """ Displays the form (GET request) and takes the data from the form,
    validates it and awards the user points.
    """
    if validate_user_ip(request) is False:
        messages.error(request, ("Must be on Exeter campus to submit images!"))

    # Checks if request is after submitting form or before
    if request.method == 'POST':
        # Recreates the form with the posted data
        form = ImageForm(request.POST, request.FILES)

        # Checks the submission has all valid fields
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance

            # Get the username of the logged in user
            username = request.user.username
            # TODO: Different numbers of points for different rooms.
            # TODO: Add validation.
            addPoints(username, 1)

            return render(request, 'UI/submission.html', 
                          {'form': form})
    else:
        # If not already submitted will create a new image form
        form = ImageForm()
    # Will return the formatted index.html file with the form entered
    return render(request, 'UI/submission.html', {'form': form})

@login_required
def working_submission_view(request):
    """ Displays the form (GET request) and takes the data from the form,
    validates it and awards the user points.
    """
    if validate_user_ip(request) is False:
        messages.error(request, ("Must be on Exeter campus to submit images!"))

    # Checks if request is after submitting form or before
    if request.method == 'POST':
        # Recreates the form with the posted data
        form = ImageForm(request.POST, request.FILES)

        # Checks the submission has all valid fields
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance

            # Get the username of the logged in user
            username = request.user.username
            # TODO: Different numbers of points for different rooms.
            # TODO: Add validation.
            addPoints(username, 1)

            return render(request, 'submission/index.html', 
                          {'form': form})
    else:
        # If not already submitted will create a new image form
        form = ImageForm()
    # Will return the formatted index.html file with the form entered
    return render(request, 'submission/index.html', {'form': form})


def validate_user_ip(request):
    """
    """
    forwarded_ips = request.META.get('HTTP_X_FORWARDED_FOR')
    # Get the users IP
    if forwarded_ips is not None:
        user_ip = forwarded_ips.split(',')[-1].strip()
    else:
        user_ip = request.META.get('REMOTE_ADDR')

    # Validate that it is in the range of possible IPs on the university
    # campus
    if "10.173.80" in user_ip:
        return True
    else:
        return False
