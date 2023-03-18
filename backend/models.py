from django.db import models

# Create your models here.

class Changes(models.Model):
    email_zeit = models.PositiveIntegerField(null=True)
    email_betreff = models.CharField(max_length=100, null=True)
    email_text = models.TextField(null=True)

def __str__(self):
    return self.email_betreff + " " + self.email_zeit