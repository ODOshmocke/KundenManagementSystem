from django.db import models

# Create your models here.

class email_information(models.Model):
    email_zeit = models.PositiveIntegerField(null=True)
    email_betreff = models.CharField(max_length=100, null=True)
    email_text = models.TextField(null=True)

class email_senden:
    email_zeit = models.PositiveBigIntegerField(null=True)

def __str__(self):
    return self.email_betreff + " " + self.email_zeit
