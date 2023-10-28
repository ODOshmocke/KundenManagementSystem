from django import forms

class UnterschriftFormular(forms.Form):
    unterschrift = forms.ImageField(label="Unterschrift", required=False)
    verbindungsCode = forms.IntegerField(label="Verbindungscode", required=False)