from django.forms import ModelForm
from .models import emailInformation


class CreateEmailDelayForm(ModelForm):

    class Meta:

        model = emailInformation
        fields = ['emailBetreff', 'emailText', 'anzahlTageZumSenden']
        labels = {
            'email_betreff': 'Betreff',
            'email_text': 'Hier den Email inhalt eingeben',
            'email_zeit': 'Die anzahl der Tage, nach dem die Email gesendet werden soll'
        }
