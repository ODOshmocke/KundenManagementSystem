from django import forms
from django.forms import ModelForm
from .models import UnterschriftsVerknuepfung
from .models import Leistungserbringer

class UnterschriftFormular(forms.Form):
    unterschrift = forms.ImageField(label="Unterschrift", required=False)
    verbindungsCode = forms.IntegerField(label="Verbindungscode", required=False)

class UnterschriftsVerknuepfungForm(ModelForm):
    class Meta:
        model = UnterschriftsVerknuepfung
        exclude = "__all__"

class LeistungserbringerFormular(ModelForm):

    vorname = forms.CharField(label="Vorname", required=False)
    nachname = forms.CharField(label="Nachname", required=False)
    ort = forms.CharField(label="Ort", required=False)
    class Meta:
        model = Leistungserbringer
        fields = "__all__"
