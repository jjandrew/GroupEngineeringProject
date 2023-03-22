""" Outlines the structure and content of the submission form. """
from django import forms
from submission.models import ImageSubmission


class ImageForm(forms.ModelForm):
    """ Creates a form using the image submission model and includes all the
    fields.

    formsl.ModelForm (ModelForm): The Django Form object used to create the
        image submission form.
    """

    class Meta:
        """ A class that talks about the sign up class, enabling further
        validators to be created.
        """
        model = ImageSubmission
        fields = ('building', 'room', 'lights_status',
                  'windows_status', 'litter_items', 'image')
