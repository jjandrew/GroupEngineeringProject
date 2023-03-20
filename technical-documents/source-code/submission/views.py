from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import ImageForm
from accounts.models import CustomUser
from submission.crowd_source import input_stats
from submission.models import ImageSubmission
from datetime import datetime, timedelta
from leaderboard.models import BuildingModel


def calcPoints(buildingName):
    """Gives a points for each day since a building has been checked"""
    # Get the building model
    # Definitely created as this is checked when stats are input
    building = BuildingModel.objects.get(name=buildingName)
    # Get todays date and difference between
    today = datetime.today()
    last_done = building.last_done.replace(tzinfo=None)
    td = today - last_done
    days_since = td.days
    # If difference less than 1 due to default value then make points worth 1
    if last_done.year == 2023 and last_done.month == 1:
        days_since = 1
    if days_since < 1:
        days_since = 1
    building.last_done = today
    building.save()
    return days_since



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


def calc_user_streaks(user, today):
    # Check if user submitted a room yesterday
    yesterday = today - timedelta(days=1)
    if user.last_submission.strftime('%Y-%m-%d') == yesterday.strftime('%Y-%m-%d'):
        user.streak += 1
    elif user.last_submission.strftime('%Y-%m-%d') < yesterday.strftime('%Y-%m-%d'):
        user.streak = 1
    user.last_submission = today.strftime('%Y-%m-%d')

    user.save()


@login_required
def submission_view(request):
    """ Displays the form (GET request) and takes the data from the form,
    validates it and awards the user points.
    """
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
            points = calcPoints(image_submission.building)
            addPoints(username, points)

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
    # Checks if request is after submitting form or before
    if request.method == 'POST':
        # Recreates the form with the posted data
        form = ImageForm(request.POST, request.FILES)

        # Checks the submission has all valid fields
        if form.is_valid():
            # Get the current instance object to display in the template

            # Gets the data fro the form
            data = form.cleaned_data

            # Gets username of logged in user
            username = request.user.username

            # Create an image submission model of this
            image_submission = ImageSubmission(building=data["building"], room=data["room"],
                                               lights_status=data["lights_status"],
                                               windows_status=data["windows_status"],
                                               litter_items=data["litter_items"], image=data["image"],
                                               user=username, date=datetime.today().strftime('%Y-%m-%d'))

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
            addPoints(username, 1)

            # Maybe reset the form?
            return render(request, 'submission/index.html',
                          {'form': form, 'message': message})
    else:
        # If not already submitted will create a new image form
        form = ImageForm()
    # Will return the formatted index.html file with the form entered
    return render(request, 'submission/index.html', {'form': form})
