from django.shortcuts import render
from .forms import CreateEmailDelayForm
from django.apps import apps
from django.db.utils import OperationalError
from django.db import models
from register.models import UserInformation


def dashboard(request):
    if request.method == 'POST':
        print("POST")

        form = CreateEmailDelayForm(request.POST)

        if form.is_valid():
            obj = form.save()  # Objekt in der Datenbank speichern und zurückgeben
            obj_id = obj.id  # ID des Objekts abrufen
            print(obj_id)
            new_email = {obj_id: False}

            alleKunden = UserInformation.objects.all()
            for kunden in alleKunden:
                kunden.emailDaten.update(new_email)
                kunden.save()


    else:
        form = CreateEmailDelayForm()

    return render(request, 'indexDashboard.html', {'form': form})
