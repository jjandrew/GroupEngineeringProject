from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import ImageForm
from accounts.models import CustomUser
from submission.crowd_source import input_stats
from submission.models import ImageSubmission
from datetime import datetime


is_repeat = False
last_room = None
last_building = None


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
    # Checks if request is after submitting form or before
    if request.method == 'POST':
        # Recreates the form with the posted data
        form = ImageForm(request.POST, request.FILES)

        # Checks the submission has all valid fields
        if form.is_valid():
            # Get the current instance object to display in the template

            # Gets the data fro the form
            data = form.cleaned_data

            username = request.user.username

            # Create an image submission model of this
            image_submission = ImageSubmission(building=data["building"], room=data["room"],
                                               number_of_lights=data["number_of_lights"], number_lights_on=data["number_lights_on"],
                                               number_of_windows=data["number_of_windows"], number_windows_open=data["number_windows_open"],
                                               number_plugs=data["number_plugs"], number_plugs_on=data["number_plugs_on"],
                                               litter_items=data["litter_items"], image=data["image"],
                                               user=username, date=datetime.today().strftime('%Y-%m-%d'))

            # Get the session variables to check if repeated entry
            is_repeat = request.session.get("repeat")
            last_room = request.session.get("last_room")
            last_building = request.session.get("last_building")
            # If a user changes submission resets the is_repeat variable
            if not is_repeat or not last_building or not last_room:
                is_repeat = False
            if last_building != image_submission.building or last_room != image_submission.room:
                is_repeat = False
                request.session['repeat'] = False
                request.session['last_building'] = None
                request.session['last_room'] = None

            # Checks if stats can be input and inputs if so
            is_input = input_stats(image_submission, is_repeat)
            message = None
            if is_input == "complete":
                # Before being saved need gamekeeper verification
                # TODO not sure when to save this
                image_submission.save()
                message = "Success"
            elif is_input == "check":
                # Ask user to recheck and then if still different change
                message = "Your room stats differ slightly please recheck"
                request.session["repeat"] = True
                request.session["last_room"] = image_submission.room
                request.session["last_building"] = image_submission.building
            else:
                # print error message
                message = "Error: the stats entered are invalid"

            # Get the username of the logged in user
            username = request.user.username
            # TODO: Different numbers of points for different rooms.
            # TODO: Add validation.
            addPoints(username, 1)

            return render(request, 'submission/index.html',
                          {'form': form, 'message': message})
    else:
        # If not already submitted will create a new image form
        form = ImageForm()
    # Will return the formatted index.html file with the form entered
    return render(request, 'submission/index.html', {'form': form})
