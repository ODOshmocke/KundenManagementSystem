from django.shortcuts import render
from .forms import CreateEmailDelayForm
from django.apps import apps
from django.db.utils import OperationalError
from django.db import models
from register.models import UserInformation


def backend(request):

    if request.method == 'POST':
        print("POST")

        form = CreateEmailDelayForm(request.POST)

        if form.is_valid():
            obj = form.save()  # Objekt in der Datenbank speichern und zurückgeben
            obj_id = obj.id  # ID des Objekts abrufen
            print(obj_id)
            new_email = {obj_id: False}


            all_users = UserInformation.objects.all()
            for user in all_users:
                user.gesendet.update(new_email)
                user.save()


    else:
        form = CreateEmailDelayForm()
        print("GET")



    return render(request, 'indexBackend.html', {'form' : form})

