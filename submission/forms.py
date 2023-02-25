from django import forms
from .models import ImageSubmission


class ImageForm(forms.ModelForm):
    # Creates a form using the image submission model and includes all fields
    class Meta:
        model = ImageSubmission
        fields = '__all__'
