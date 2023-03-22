from django.shortcuts import render
import random

from django.shortcuts import render
from accounts.models import CustomUser
from datetime import date
from django.shortcuts import render
from django.views import View
# Create your views here.


def get_daily_task(user):


    # Check if the user has a daily task assigned for today
    if user.last_daily_task != date.today():
        # Generate a new daily task and assign it to the user

        user.daily_task = random.randint(0, 43)#44 options
        user.last_daily_task = date.today()
        user.save()


def index(request):
    user = request.user
    #get_daily_task(user)



    building_choices = ['Alexander','Amory', 'Business School Building:One','Byrne House', 'Clayden',
                        'Clydesdale House','Cornwall House','Cornwall House Swimming Pool','Devonshire House',
                        'Estate Service Centre','Family Centre (Owlets)','Forum and Library','Geoffrey Pope',
                        'Great Hall and University Reception','Harrison','Hatherly','Henry Wellcome Building for Biocatalysis',
                        'Innovation Centre Phase 1 and 2','Institute of Arab and Islamic Studies','INTO International Study Centre',
                        'Kay House Duryard','Knightley','Lafrowda House','Laver','Lazenby','Mary Harris Memorial Chapel','Newman',
                        'Northcote House','Northcott Theatre','Old Library','Peter Chalk Centre','Physics',"Queen's",'Redcot','Reed Hall',
                        'Reed Mews Wellbeing Centre','Roborough','Russell Seal Fitness Centre','Sir Christopher Ondaatje Devon Cricket Centre',
                        'Sir Henry Wellcome Building for Mood Disorders Research','Streatham Court','Streatham Farm','Washington Singer','Xfi']

    taskNumber = user.daily_task
    task1 = building_choices[taskNumber]


    args = {'task1': task1}
    return render(request, "homepage/homepage.html", args)