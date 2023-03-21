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
from gkHomepage.crowd_source import input_stats
from leaderboard.co2_calcs import get_co2
import pytz


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


def get_top_submission():
    """Gets the submission at the top of the ImageSubmission model"""
    top_submission = ImageSubmission.objects.order_by('-id').first()
    if top_submission:
        return top_submission
    return None


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
    images = ImageSubmission.objects.all
    print(ImageSubmission.objects.all().count())
    args = {'images': images}
    if ImageSubmission.objects.all().count() > 0:

        if request.method == 'POST' and 'action_btn_accept' in request.POST:
            print("----", "YOU'VE PRESSED ACCEPT")
            images = ImageSubmission.objects.exclude(
                id=ImageSubmission.objects.first().id)
            args = {'images': images, 'name': 'Building'}

            top_sub = get_top_submission()

            # Calculate statistics for user
            if top_sub == None:
                return render(request, "gkHomepage/gkHomepage.html", args)
            username = top_sub.user
            user = CustomUser.objects.get(username=username)

            building_name = get_building_name(top_sub)

            args['name'] = building_name

            calc_user_streaks(user, datetime.today())
            print("----", top_sub.building)
            points = calcPoints(top_sub.building)
            addPoints(username, points)

            # Checks if stats can be input and inputs if so
            input_stats(top_sub)

            get_co2(top_sub, top_sub.building)
            ImageSubmission.objects.all().first().delete()
            return render(request, "gkHomepage/gkHomepage.html", args)

        if request.method == 'POST' and 'action_btn_delete' in request.POST:
            print("----", "YOUVE PRESSED DELETE")
            ImageSubmission.objects.all().first().delete()

            top_sub = get_top_submission()
            name = get_building_name(top_sub)

            args = {'images': images, 'name': name}
            return render(request, "gkHomepage/gkHomepage.html", args)

        if request.method == 'POST' and 'action_btn_report' in request.POST:
            print("----", "YOUVE PRESSED REPORT")
            ImageSubmission.objects.all().first().delete()
            # TODO write a mockup email with image, name of user, email of user, date etc and save to file.

            image_filename = '04d.png'
            image_path = os.path.abspath(os.path.join(
                os.path.dirname(__file__), image_filename))
            msg = EmailMessage()
            msg['Subject'] = 'Image Report'
            msg['From'] = 'thegreenmasterproject@gmail.com'
            msg['To'] = 'louislusso@hotmail.com'
            msg.set_content('Please find the attached image report.')
            with open(image_path, 'rb') as f:
                file_data = f.read()
                file_name = os.path.basename(image_path)
                msg.add_attachment(file_data, maintype='image',
                                   subtype='png', filename=file_name)
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.starttls()
                smtp.login('thegreenmasterproject@gmail.com',
                           'bkstedudehhuuetb')
                # bkstedudehhuuetb
                smtp.send_message(msg)
            print("----", 'Email sent.')

            images = ImageSubmission.objects.all

            top_sub = get_top_submission()
            name = get_building_name(top_sub)

            args = {'images': images, 'name': name}

            args = {'images': images}
            return render(request, "gkHomepage/gkHomepage.html", args)

        return render(request, "gkHomepage/gkHomepage.html", args)

    return render(request, "gkHomepage/gkHomepage.html", args)
