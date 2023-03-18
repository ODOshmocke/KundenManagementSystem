from django.forms import ModelForm
from .models import Changes


class CreateEmailDelayForm(ModelForm):

    class Meta:

        model = Changes
        fields = ['email_betreff','email_text', 'email_zeit']
        labels = {
            'email_betreff': 'Betreff',
            'email_text': 'Hier den Email inhalt eingeben',
            'email_zeit': 'Die anzahl der Tage, nach dem die Email gesendet werden soll'
        }
