from django.forms import ModelForm
from .models import UserInformation
from django import forms
from django.conf import settings


class UserInformationForm(ModelForm):
    geburtsdatum = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}),
                                   input_formats=settings.DATE_INPUT_FORMATS)


    class Meta:
        model = UserInformation


        exclude = ['erstellt', 'emailDaten']

