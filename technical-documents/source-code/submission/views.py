""" Outlines the method to be used by the submission app. """
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from accounts.models import CustomUser
from leaderboard.models import BuildingModel
from gkHomepage.crowd_source import input_stats
from submission.models import ImageSubmission, RoomModel
from submission.forms import ImageForm
from datetime import datetime, timedelta
from leaderboard.models import BuildingModel


def calc_points(building_name: str) -> int:
    """ Gives points for each day since a building has been checked

    Args:
        buildingName (str): The name of the building to calculate points for
            provided as a string for readability.

    Returns:
        int: days_since: The number of days since a building has been checked,
            given as an integer.
    """
    # Get the building model
    # Definitely created as this is checked when stats are input
    building = None
    if not BuildingModel.objects.filter(name=building_name).exists():
        building = BuildingModel(name=building_name)
        building.save()
    else:
        building = BuildingModel.objects.get(name=building_name)
    # Get todays date and difference between
    today = datetime.today()
    last_done = building.last_done.replace(tzinfo=None)
    t_d = today - last_done
    days_since = t_d.days
    # If difference less than 1 due to default value then make points worth 1
    if last_done.year == 2023 and last_done.month == 1:
        days_since = 1
    if days_since < 1:
        days_since = 1
    building.last_done = today
    building.save()
    return days_since


def add_points(username: str, points: int) -> None:
    """ Lets the user enter points, and validates the points they enter into
    the form; to execute this function, the user must be logged in.

    Args:
        username (str): The name of user to award points to, given as a string
            for convenience.
        points (int): The number of points to be awarded to the user, as an
            integer.
    """
    # Check if user already has a score entered
    if points <= 0:
        raise RuntimeError("Can't add negative points")

    # Add the points to a user's points
    user = CustomUser.objects.get(username=username)
    user.points += points
    user.save()


def calc_user_streaks(user: CustomUser, today: datetime) -> None:
    """ Calculates the streaks for a given user.

    Args:
        user (CustomUser): The user to calculate the streak for, given as a
            CustomUser object.
        today (datetime): The current date given as a date time type to enable
            calculations and operations with the value.
    """
    # Check if user submitted a room yesterday
    yesterday = today - timedelta(days=1)
    if user.last_submission.strftime('%Y-%m-%d') == \
            yesterday.strftime('%Y-%m-%d'):
        user.streak += 1
    elif user.last_submission.strftime('%Y-%m-%d') < \
            yesterday.strftime('%Y-%m-%d'):
        user.streak = 1
    user.last_submission = today.strftime('%Y-%m-%d')

    user.save()


@login_required
def submission_view(request):
    """ The webpage and page validation for image submissions. Note, the user
    must be logged in to see the page.

    Args:
        request : The web request the user has made that needs to be
            processed.
    Returns:
        render(): The webpage to be displayed to the user.
    """
    # Checks if request is after submitting form or before
    if request.method == 'POST':
        # Recreates the form with the posted data
        form = ImageForm(request.POST, request.FILES)

        # Checks the submission has all valid fields
        if form.is_valid():
            form.save()

            # Get the username of the logged in user
            username = request.user.username

            return render(request, 'UI/submission.html',
                          {'form': form})
    else:
        # If not already submitted will create a new image form
        form = ImageForm()
    # Will return the formatted index.html file with the form entered
    return render(request, 'UI/submission.html', {'form': form})


@login_required
def working_submission_view(request):
    
    if request.method == 'POST':

        uploadedFile = request.FILES["subFile"]

        print(uploadedFile.name)

    return render(request, 'UI/submissionNEW.html')

    """ The webpage and page validation for image submissions. Note, the user
    must be logged in to see the page.

    Args:
        request : The web request the user has made that needs to be
            processed.
    Returns:
        render(): The webpage to be displayed to the user.
    """
    # Checks if request is after submitting form or before
    """
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
            if not skip:
                # Check if done an hour before
                hour_ago = (datetime.now() - timedelta(hours=1))
                if room.last_done.replace(tzinfo=None) > hour_ago:
                    return render(request, 'submission/index.html',
                                  {'form': form, 'message': "Error: room submitted too recently"})

            # Check if a room has been submitted in the last hour
            # Get the room
            room = None
            skip = False
            if RoomModel.objects.filter(building=image_submission.building, name=image_submission.room.lower()).exists():
                room = RoomModel.objects.get(
                    name=image_submission.room.lower(), building=image_submission.building)
            else:
                skip = True
            if not skip:
                # Check if done an hour before
                hour_ago = (datetime.now() - timedelta(hours=1))
                if room.last_done.replace(tzinfo=None) > hour_ago:
                    return render(request, 'submission/index.html',
                                  {'form': form, 'message': "Error: room submitted too recently"})

            image_submission.save()

            # TODO VALIDATION HERE

            # Calculate statistics for user
            user = CustomUser.objects.get(username=username)

            calc_user_streaks(user, datetime.today())

            # Checks if stats can be input and inputs if so
            input_stats(image_submission)

            # TODO this is where gamekeeper validation occurs

            message = "Success"

            # TODO: Different numbers of points for different rooms.
            # TODO: Add validation.
            points = calc_points(image_submission.building)
            add_points(username, points)

            # Maybe reset the form?
            return render(request, 'submission/index.html',
                          {'form': form, 'message': message})
    else:
        # If not already submitted will create a new image form
        form = ImageForm()
    # Will return the formatted index.html file with the form entered
    return render(request, 'submission/index.html', {'form': form})
"""