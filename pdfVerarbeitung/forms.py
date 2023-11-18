from django import forms
from django.forms import ModelForm
from .models import UnterschriftsVerknuepfung

class UnterschriftFormular(forms.Form):
    unterschrift = forms.ImageField(label="Unterschrift", required=False)
    verbindungsCode = forms.IntegerField(label="Verbindungscode", required=False)

class UnterschriftsVerknuepfungForm(ModelForm):
    class Meta:
        model = UnterschriftsVerknuepfung
        exclude = "__all__"
