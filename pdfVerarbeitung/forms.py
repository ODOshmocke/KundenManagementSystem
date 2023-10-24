from django import forms

class UnterschriftFormular(forms.Form):
    unterschrift = forms.CharField(max_length=200)
