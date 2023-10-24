from django.forms import ModelForm
from .models import KundenDaten
from django import forms
from django.conf import settings


class kundenDatenForm(ModelForm):
    geburtsdatum = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}),
                                   input_formats=settings.DATE_INPUT_FORMATS)


    class Meta:
        model = KundenDaten


        exclude = ['erstellt', 'emailDaten']

