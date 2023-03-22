""" Outlines the methods used by the submission page(s). """
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
from accounts.models import CustomUser
from submission.models import ImageSubmission, RoomModel
from submission.forms import ImageForm


def calc_user_streaks(user: CustomUser, today: datetime):
    """ Calculates the streaks for a user.

    Args:
        user: (CustomUser): The user object corresponding to the user having
            their streaks calculated.
        today: (dateTime): Helps calculate the streak, the current date given
            as the current date/ time.
    """
    # Check if user submitted a room yesterday
    yesterday = today - timedelta(days=1)
    if user.last_submission.strftime('%Y-%m-%d') == yesterday.strftime('%Y-%m-%d'):
        user.streak += 1
    elif user.last_submission.strftime('%Y-%m-%d') < yesterday.strftime('%Y-%m-%d'):
        user.streak = 1
    # print(user.last_submission.type())
    user.last_submission = today.strftime('%Y-%m-%d')

    user.save()


@login_required
def working_submission_view(request):
    """ The webpage and page validation for image submissions. Note, the user
    must be logged in to see the page.

    Args:
        request : The web request the user has made that needs to be
            processed.
    Returns:
        render(): The webpage to be displayed to the user.
    """

    # Verifies that the user is making a submission from campus
    if validate_user_ip(request) is False:
        messages.error(request, ("Must be on Exeter campus to submit images!"))

    # Checks if request is after submitting form or before
    if request.method == 'POST':
        # Recreates the form with the posted data
        form = ImageForm(request.POST, request.FILES)

        # Checks the submission has all valid fields
        if form.is_valid():
            # Get the current instance object to display in the template

            # Gets the data from the form
            data = form.cleaned_data
            # Gets username of logged in user
            username = request.user.username

            # Create an image submission model of this
            image_submission = ImageSubmission(building=data["building"],
                                               room=data["room"],
                                               lights_status=data["lights_status"],
                                               windows_status=data["windows_status"],
                                               litter_items=data["litter_items"],
                                               image=data["image"],
                                               user=username,
                                               date=datetime.today().strftime('%Y-%m-%d'))

            # Check if a room has been submitted in the last hour
            # Get the room
            room = None
            skip = False
            if RoomModel.objects.filter(building=image_submission.building, name=image_submission.room.lower()).exists():
                room = RoomModel.objects.get(
                    name=image_submission.room.lower(), building=image_submission.building)
            else:
                skip = True
                room = RoomModel(name=image_submission.room.lower(),
                                 building=image_submission.building)
            if not skip:
                # Check if done an hour before
                hour_ago = (datetime.now() - timedelta(hours=1))
                if room.last_done.replace(tzinfo=None) > hour_ago:
                    return render(request, 'submission/index.html',
                                  {'form': form, 'message': "Error: room submitted too recently"})

            image_submission.save()

            room.last_done = datetime.now()
            room.save()

            # Calculate statistics for user
            user = CustomUser.objects.get(username=username)

            calc_user_streaks(user, datetime.today())

            message = "Success"

            # Maybe reset the form?
            return render(request, 'submission/index.html',
                          {'form': form, 'message': message})
    else:
        # If not already submitted will create a new image form
        form = ImageForm()
    # Will return the formatted index.html file with the form entered
    return render(request, 'submission/index.html', {'form': form})


def validate_user_ip(request):
    """ Extracts the user's IP address from the provided HTTP request and
    uses it to validate that they are making a submission from campus.

    Args:
        request: The HTTP request submitted by the user.

    Returns:
        bool: True/ False: A boolean value indicating whether the user's IP
            is in the range of IP's provided by the campus wifi.
    """
    forwarded_ips = request.META.get('HTTP_X_FORWARDED_FOR')
    # Get the user's IP
    if forwarded_ips is not None:
        user_ip = forwarded_ips.split(',')[-1].strip()
    else:
        user_ip = request.META.get('REMOTE_ADDR')

    # Validate that it is in the range of possible IPs on the university
    # campus or from the local host
    if '144.173.23' in user_ip or '127.0.0' in user_ip:
        # 10.173.80
        return True
    else:
        return False
