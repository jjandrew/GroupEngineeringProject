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
        fields = ('building', 'room', 'number_of_lights', 'number_lights_on', 'number_of_windows',
                  'number_windows_open', 'number_plugs', 'number_plugs_on', 'litter_items', 'image')
