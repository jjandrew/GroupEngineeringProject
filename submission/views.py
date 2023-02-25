from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ImageForm


def submission_view(request):
    # Checks if request is after submitting form or before
    if request.method == 'POST':
        # Recreates the form with the posted data
        form = ImageForm(request.POST, request.FILES)
        # Checks the submission has all valid fields
        if form.is_valid():
            print(form.data)
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'submission/index.html', {'form': form, 'img_obj': img_obj})
    else:
        # If not already submitted will create a new image form
        form = ImageForm()
    # Will return the formatted index.html file with the form entered
    return render(request, 'submission/index.html', {'form': form})
