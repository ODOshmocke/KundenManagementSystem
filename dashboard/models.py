from django.db import models


# Create your models here.

class emailInformation(models.Model):
    anzahlTageZumSenden = models.PositiveIntegerField(null=True)
    emailBetreff = models.CharField(max_length=100, null=True)
    emailText = models.TextField(null=True)


def __str__(self):
    return self.emailBetreff + " " + self.anzahlTageZumSenden

