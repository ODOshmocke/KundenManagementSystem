from django.db import models
import django


class UserInformation(models.Model):
    nachname = models.CharField(max_length=200)
    vorname = models.CharField(max_length=200)
    email = models.EmailField()
    telefon = models.CharField(max_length=200)
    strasse = models.CharField(max_length=200)
    ort_plz = models.CharField(max_length=200)
    krankenkasse = models.CharField(max_length=200)
    geburtsdatum = models.DateField(default=django.utils.timezone.now)
    erstellt = models.DateTimeField(default=django.utils.timezone.now)
    geschlecht = models.CharField(choices=(('Mann', 'Mann'), ('Frau', 'Frau'), ('nicht definiert', 'nicht definiert')), max_length=20, default="nicht definiert")
    notiz = models.CharField(blank=True, null=True, max_length=1000)


    emailDaten = models.JSONField(null=True, blank=True)






def __str__(self):
        return self.nachname + " " + self.vorname
