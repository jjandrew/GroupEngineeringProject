from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from accounts.models import CustomUser
from leaderboard.models import BuildingModel
from django.contrib import messages
from gkHomepage.crowd_source import input_stats
from submission.models import ImageSubmission, RoomModel
from submission.forms import ImageForm
from datetime import datetime, timedelta


def calc_user_streaks(user: CustomUser, today: datetime):
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
def submission_view(request):
    """ Displays the form (GET request) and takes the data from the form,
    validates it and awards the user points.
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
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance

            # Get the username of the logged in user
            username = request.user.username
            # TODO: Different numbers of points for different rooms.
            # TODO: Add validation.

            return render(request, 'UI/submission.html',
                          {'form': form})
    else:
        # If not already submitted will create a new image form
        form = ImageForm()
    # Will return the formatted index.html file with the form entered
    return render(request, 'UI/submission.html', {'form': form})


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

    if request.method == 'POST':
        uploadedFile = request.FILES["subFile"]
       # print(uploadedFile.name)
        return render(request, 'UI/submissionNEW.html')


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
            image_submission = ImageSubmission(building=data["building"], room=data["room"],
                                               lights_status=data["lights_status"],
                                               windows_status=data["windows_status"],
                                               litter_items=data["litter_items"], image=data["image"],
                                               user=username, date=datetime.today().strftime('%Y-%m-%d'))

            image_submission.save()

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
    if '10.173.80' in user_ip or '127.0.0' in user_ip:
        return True
    else:
        return False

