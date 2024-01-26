from django.shortcuts import render
from .forms import UnterschriftFormular
from .forms import UnterschriftsVerknuepfungForm
from django.http import JsonResponse
import base64
from django.core.files.base import ContentFile
from .models import GeradeAngemeldet


def unterschriftView(request, unterschriftsDaten=None):

    print(unterschriftsDaten, "unterschriftsDaten")


    if request.method == "POST" or request.method == "FILES":
        unterschriftFormular = UnterschriftFormular(request.POST)
        unterschriftsVerknuepfung = UnterschriftsVerknuepfungForm(request.POST)


        if unterschriftFormular.is_valid() and unterschriftsVerknuepfung.is_valid():

            verbindungsCode = request.POST.get("connection_code")


            #Bild wird in base64 codiert und in ein Bild umgewandelt
            canvas_data = request.POST.get("canvasData")
            canvas_data = canvas_data.replace("data:image/png;base64,", "")
            binary_data = base64.b64decode(canvas_data)


            #Irgendwas sagt mir das es hier einen Fehler geben wird
            #Mit dem COde wird das Bild in der Datenbank gespeichert

            unterschrift_verknuepfung = unterschriftsVerknuepfung.save(commit=False)
            unterschrift_verknuepfung.verbindungsCode = verbindungsCode

            #Es wird geschaut ob es sich um eine Unterschrift vom einem Leistungserbringer handelt
            if unterschriftsDaten != None:
                unterschrift_verknuepfung.unterschriftPfad.save(f"leistungserbringer/{verbindungsCode}_unterschrift.png", ContentFile(binary_data))
            else:
                unterschrift_verknuepfung.unterschriftPfad.save(f"{verbindungsCode}_unterschrift.png", ContentFile(binary_data))# das sieht sehr sketchy aus

            unterschrift_verknuepfung.save()
            GeradeAngemeldet.objects.create(verbindungsCode=verbindungsCode)
            print("Unterschrift wurde gespeichert")


            '''bildPfad = "unterschrift.png"

            with open(bildPfad, "wb") as fh:
                fh.write(binary_data)'''


    else:
        unterschriftFormular = UnterschriftFormular()
        UnterschriftsVerknuepfung = UnterschriftsVerknuepfungForm()

    return render(request, "unterschrift.html", {"unterschriftFormular": unterschriftFormular})


def unterschriftsBestaetigungView(request):
    verbindungsCodeRegister = int(request.POST.get("verbindungsCode"))
    verbindungsCodesDatenbank = list(GeradeAngemeldet.objects.values_list("verbindungsCode", flat=True))
    if verbindungsCodeRegister in verbindungsCodesDatenbank:
        print("Unterschrift bestätigt")
        return JsonResponse({"bestätigt": True})
    else:
        print("Unterschrift nicht bestätigt")
        return JsonResponse({"bestätigt": False})
