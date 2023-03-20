from django.shortcuts import render
from submission.models import ImageSubmission
from django.http import HttpResponse
from accounts.models import CustomUser
import email
import smtplib
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.core.mail import send_mail
from datetime import datetime, timedelta
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
    top_submission = ImageSubmission.objects.order_by('-id').first()
    if top_submission:
        return top_submission.user
    return None

def report_user(userEmail,date,image,filename):
    msg = email.mime.text.MIMEText('Dear Campus services,It has come to our attention that a user, under the email '+userEmail+
                                   'has used our platform to send the following image attached on '+date +
                                   'We have now removed the user from our platform and trust you will deal with this'+
                                   'appropriately')
    #msg.attach(MIMEText('<html><body>' +
     #                   '<p><img src="'+image+'"></p>' +
     #                   '</body></html>', 'html', 'utf-8'))
    msg['Subject'] = 'Inapropriate images being uploaded to Exeters Green Master app'
    msg['From'] = 'gamekeeper@exeter.ac.uk'
    msg['To'] = 'CampusServices@exeter.ac.uk'
    filename = filename +".elm"
    # open a file and save mail to it
    file = open("/../../reportedEmails/filename.elm", "w")
    gen = email.generator.Generator(file)
    gen.flatten(msg)
def index(request):
    images = ImageSubmission.objects.all
    print(ImageSubmission.objects.all().count())
    args = {'images': images}
    if ImageSubmission.objects.all().count()>0:


        if request.method == 'POST' and 'action_btn_accept' in request.POST:
            print("----", "YOU'VE PRESSED ACCEPT")
            images = ImageSubmission.objects.exclude(id=ImageSubmission.objects.first().id)
            args = {'images': images}
            #username = get_top_username()
            #addPoints(username, 1)
            ImageSubmission.objects.all().first().delete()
            return render(request, "gkHomepage/gkHomepage.html", args)

        if request.method == 'POST' and 'action_btn_delete' in request.POST:
            print("----","YOUVE PRESSED DELETE")
            ImageSubmission.objects.all().first().delete()
            args = {'images': images}
            return render(request, "gkHomepage/gkHomepage.html", args)

        if request.method == 'POST' and 'action_btn_report' in request.POST:
            print("----","YOUVE PRESSED REPORT")
            ImageSubmission.objects.all().first().delete()
            #TODO write a mockup email with image, name of user, email of user, date etc and save to file.
            args = {'images': images}
            return render(request, "gkHomepage/gkHomepage.html", args)

        return render(request, "gkHomepage/gkHomepage.html", args)
    else:
        ImageSubmission(building="No Building Left", room="No Room Left",
                                           lights_status="OFF",
                                           windows_status="CLOSED",
                                           litter_items= 0, image="/../../updated UI/img/defaultimage.jpg",
                                           user="NONE", date=datetime.today().strftime('%Y-%m-%d'))
        images = ImageSubmission.objects.all
        args = {'images': images}
        #TODO crate a object thats the standard object or set it as standard object
        return render(request, "gkHomepage/gkHomepage.html", args)
