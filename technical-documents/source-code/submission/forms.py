""" Outlines the class to create the submission form to be displayed. """
from django import forms
from submission.models import ImageSubmission


class ImageForm(forms.ModelForm):
    """ Creates a form using the image submission model and includes all the
    fields.

    Args:
        forms.ModelForm (ModelForm): The base django form to be returned to
            the user.
    """

    class Meta:
        """ A class that talks about the sign up class, enabling further
        validators to be created.
        """
        model = ImageSubmission
        fields = ('building', 'room', 'lights_status',
                  'windows_status', 'litter_items', 'image')
