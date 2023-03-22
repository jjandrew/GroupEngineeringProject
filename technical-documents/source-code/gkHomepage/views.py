from django.shortcuts import render
from submission.models import ImageSubmission, building_choices
from leaderboard.models import BuildingModel
from accounts.models import CustomUser
from django.core.mail import EmailMessage
from django.conf import settings
from datetime import datetime, timedelta
import os
import smtplib
from email.message import EmailMessage
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from gkHomepage.crowd_source import input_stats
from leaderboard.co2_calcs import get_co2


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


def get_top_username():
    """Gets the username of the user that sumbitted the image which the
    gamekeeper is currently reviewing
    """
    top_submission = ImageSubmission.objects.order_by('-id').first()
    # check if there is a image the gamekeeper is reviewing
    if top_submission:
        # if there is then return the username of whoever uploaded that image
        return top_submission.user
    return None


def get_top_email():
    """Gets the email of the user that sumbitted the image which the
        gamekeeper is currently reviewing
        """
    top_submission = ImageSubmission.objects.order_by('-id').first()
    # check if there is a image the gamekeeper is reviewing
    if top_submission:
        # if there is then return the email of whoever uploaded that image
        email = CustomUser.objects.get(username=top_submission.user).email
        return email
    return None


def get_top_submission():
    """Gets the full object of the user that sumbitted the image which the
            gamekeeper is currently reviewing
            """
    top_submission = ImageSubmission.objects.order_by('-id').first()
    # check if there is a image the gamekeeper is reviewing
    if top_submission:
        # if there is then return the full object of whoever uploaded that image
        return top_submission
    return None


def get_building_name(top_sub):
    # Translate Constant building name to formatted string
    building_name = None
    for choice in building_choices:
        if choice[0] == top_sub.building:
            building_name = choice[1]
            break
    if building_name == None:
        # TODO remove this
        print("Collosal error")
    return building_name


def calcPoints(buildingName):
    """Gives a points for each day since a building has been checked"""
    # Get the building model
    # Definitely created as this is checked when stats are input
    building = None
    if not BuildingModel.objects.filter(name=buildingName).exists():
        building = BuildingModel(name=buildingName)
        building.save()
    else:
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


def index(request):
    """ Displays the form which displays the next image for the
    gamekeeper to verify and a few buttons to either accept the image, and therefore
    reward the points. Decline the image and finaly report the image. When an image
    is reported, an emial is generated and sent to the unviersity with the email
    of the user, date and image which the user had sent.
        """
    images = ImageSubmission.objects.all
    args = {'images': images}

    # if there is more than 0 images to review
    if ImageSubmission.objects.all().count() > 0:
        # if someone presses the accept button
        if request.method == 'POST' and 'action_btn_accept' in request.POST:
            print("----", "YOU'VE PRESSED ACCEPT")
            images = ImageSubmission.objects.exclude(
                id=ImageSubmission.objects.first().id)

            args = {'images': images, 'name': 'Building'}

            top_sub = get_top_submission()

            # Calculate statistics for user

            # get the username of the users imag
            username = get_top_username()

            if top_sub == None:
                return render(request, "gkHomepage/gkHomepage.html", args)
            username = top_sub.user

            building_name = get_building_name(top_sub)

            args['name'] = building_name

            user = CustomUser.objects.get(username=username)
            # calulate the users streak(if any)

            calc_user_streaks(user, datetime.today())

            print("----", get_top_submission().building)
            # calculate the points to give the user
            points = calcPoints(get_top_submission().building)
            # add the points to the users account
            addPoints(username, points)
            # remove that image from the database

            

            # Checks if stats can be input and inputs if so
            input_stats(top_sub)

            # Calculate the CO2 output for the building
            get_co2(top_sub, top_sub.building)

            ImageSubmission.objects.all().first().delete()
            # render the template again, checking if theres a new image to upload
            return render(request, "gkHomepage/gkHomepage.html", args)

        # if the user presses the delete button
        if request.method == 'POST' and 'action_btn_delete' in request.POST:

            print("----", "YOUVE PRESSED DELETE")
            # delete that image object from the database

            print("----", "YOUVE PRESSED DELETE")

            ImageSubmission.objects.all().first().delete()

            top_sub = get_top_submission()
            name = get_building_name(top_sub)

            args = {'images': images, 'name': name}

            # render the template again, checking if theres a new image to upload

            return render(request, "gkHomepage/gkHomepage.html", args)

        if request.method == 'POST' and 'action_btn_report' in request.POST:

            print("----", "YOUVE PRESSED REPORT")
            # get the date which the image was submitted
            date = get_top_submission().date
            # get the email of the user who submitted the image
            email = str(get_top_email())
            # get the username of the user who sumbitted the image
            username = get_top_username()
            user = CustomUser.objects.get(username=username)

            image = str(get_top_submission().image)

            print("----", image)
            # generate an email to send to the univeristy
            email = EmailMessage(
                'Inapropriate usage of GreenMaster App', 'To whom it may concern, \n'
                'You are recieving this email as one of our GameKeepers has reported this user for submitting '
                'inappropriate images into our application. \n'
                'Please find the image that was sent attached to this email. \n'
                'The users email who sent the attacked image is ' + email + ' \n'
                'This image was sent to us on ' + str(date) + ' ', 'thegreenmasterproject@gmail.com', ["louislusso@hotmail.com", ])
            # attach the image which has been reported to the email
            email.attach_file("/Users/louislusso/Library/CloudStorage/OneDrive-UniversityofExeter/Year 2/Semester 2/Software Development Project/GroupEngineeringProjectGroup4/technical-documents/source-code/media/images/04d.png")
            email.send()
            # delete the image object from the database
            ImageSubmission.objects.all().first().delete()

            print("----", "YOUVE PRESSED REPORT")




            args = {'images': images}
            # render the template again, checking if theres a new image to upload
            return render(request, "gkHomepage/gkHomepage.html", args)

        # render the template again, checking if theres a new image to upload
        return render(request, "gkHomepage/gkHomepage.html", args)
    else:
        #TODO make final image a defult one
        room = None
        user = None
        date = None
        image = "/Users/louislusso/Library/CloudStorage/OneDrive-UniversityofExeter/Year 2/Semester 2/Software Development Project/GroupEngineeringProjectGroup4/technical-documents/static/images/donkey-looking-down.jpg"
        args = {'images': images}
        return render(request, "gkHomepage/gkHomepage.html", args)
