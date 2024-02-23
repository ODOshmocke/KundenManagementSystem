from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import CreateEmailDelayForm
from django.apps import apps
from django.db.utils import OperationalError
from django.db import models
from register.models import KundenDaten
from pdfVerarbeitung.models import Leistungserbringer

import json
import urllib.parse

@login_required
def dashboard(request):
    if request.method == 'POST':
        print("POST")

        emailForm = CreateEmailDelayForm(request.POST)
        LeistungserbringerDaten = Leistungserbringer.objects.all()


        if emailForm.is_valid():
            obj = emailForm.save()  # Objekt in der Datenbank speichern und zurückgeben
            obj_id = obj.id  # ID des Objekts abrufen
            print(obj_id)
            new_email = {obj_id: False}

            alleKunden = UserInformation.objects.all()
            for kunden in alleKunden:
                kunden.emailDaten.update(new_email)
                kunden.save()


    else:
        emailForm = CreateEmailDelayForm()
        LeistungserbringerDaten = Leistungserbringer.objects.get(id=1)
        print(LeistungserbringerDaten, "LeistungserbringerDaten")

    return render(request, 'indexDashboard.html', {'form': emailForm, "LeistungserbringerDaten": LeistungserbringerDaten})


@login_required
def leistungserbringerDatenAenderung(leistungserbringerDaten):

    print(leistungserbringerDaten.POST, "leistungserbringerDaten")
    print(leistungserbringerDaten.POST.get("vorname"), "vorname")

    Leistungserbringer.objects.filter(id=1).update(
        vorname=leistungserbringerDaten.POST.get("vorname"),
        nachname=leistungserbringerDaten.POST.get("nachname"),
        adresse=leistungserbringerDaten.POST.get("adresse"))

    return JsonResponse({"bestätigt": True})






