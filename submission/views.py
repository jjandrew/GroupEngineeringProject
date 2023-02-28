from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import ImageForm
from loginApp.models import User
from accounts.models import CustomUser

@login_required
def addPoints(username, points):
    # Check if user already has a score entered
    if points <= 0:
        raise RuntimeError("Can't add negative points")
    try:
        # Add the points to a user's points
        user = CustomUser.objects.get(username=username)
        user.points += points
        user.save()
    except User.DoesNotExist:
        # Create a new user
        # TODO must change emails
        user = User(username=username, points=points, email='test@test.com',
                    first_name="testf", last_name="testl")
        user.save()

@login_required
def submission_view(request):
    # Checks if request is after submitting form or before
    if request.method == 'POST':
        # Recreates the form with the posted data
        form = ImageForm(request.POST, request.FILES)
        # Checks the submission has all valid fields
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance

            # Get the username of the logged in object
            username = request.user.username
            # For time being give each user one point per room done and no authentication:
            addPoints(username, 1)

            return render(request, 'submission/index.html', {'form': form, 'img_obj': img_obj})
    else:
        # If not already submitted will create a new image form
        form = ImageForm()
    # Will return the formatted index.html file with the form entered
    return render(request, 'submission/index.html', {'form': form})
