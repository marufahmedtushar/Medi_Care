from django import forms

from . models import Prescription_pictures


class Presform(forms.ModelForm):
    class Meta:
        model = Prescription_pictures
        fields = ('user_name', 'cover')
