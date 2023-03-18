from django import forms
from .models import ImageSubmission


class ImageForm(forms.ModelForm):
    """ Creates a form using the image submission model and includes all the 
    fields.
    """

    class Meta:
        """ A class that talks about the sign up class, enabling further
        validators to be created.
        """
        model = ImageSubmission
        fields = ('building', 'room', 'lights_status',
                  'windows_status', 'litter_items', 'image')
