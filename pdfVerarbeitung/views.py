from django.shortcuts import render
from .forms import UnterschriftFormular
from .forms import UnterschriftsVerknuepfungForm
from django.http import JsonResponse
import base64
from django.core.files.base import ContentFile
from .models import GeradeAngemeldet


def unterschriftView(request):


    if request.method == "POST" or request.method == "FILES":
        unterschriftFormular = UnterschriftFormular(request.POST)
        unterschriftsVerknuepfung = UnterschriftsVerknuepfungForm(request.POST)
        print(unterschriftFormular.is_valid(), unterschriftsVerknuepfung.is_valid())


        if unterschriftFormular.is_valid() and unterschriftsVerknuepfung.is_valid():

            verbindungsCode = request.POST.get("connection_code")

            print(verbindungsCode, "verbindungsCode")

            #Bild wird in base64 codiert und in ein Bild umgewandelt
            canvas_data = request.POST.get("canvasData")
            canvas_data = canvas_data.replace("data:image/png;base64,", "")
            binary_data = base64.b64decode(canvas_data)


            #Irgendwas sagt mir das es hier einen Fehler geben wird
            unterschrift_verknuepfung = unterschriftsVerknuepfung.save(commit=False)
            unterschrift_verknuepfung.verbindungsCode = verbindungsCode
            unterschrift_verknuepfung.unterschriftPfad.save(f"{verbindungsCode}_unterschrift.png", ContentFile(binary_data))# das sieht sehr sketchy aus
            unterschrift_verknuepfung.save()
            GeradeAngemeldet.objects.create(verbindungsCode=verbindungsCode)
            print(unterschrift_verknuepfung.unterschriftPfad.url)


            '''bildPfad = "unterschrift.png"

            with open(bildPfad, "wb") as fh:
                fh.write(binary_data)'''


    else:
        unterschriftFormular = UnterschriftFormular()
        UnterschriftsVerknuepfung = UnterschriftsVerknuepfungForm()

    return render(request, "unterschrift.html", {"unterschriftFormular": unterschriftFormular})


def unterschriftsBestaetigungView(request):
    verbindungsCodeRegister = int(request.POST.get("verbindungsCode"))
    print(verbindungsCodeRegister, "verbindungsCodeRegister")
    verbindungsCodesDatenbank = list(GeradeAngemeldet.objects.values_list("verbindungsCode", flat=True))
    print(verbindungsCodeRegister, "verbindungsCodeRegister", verbindungsCodesDatenbank, "verbindungsCodesDatenbank")
    if verbindungsCodeRegister in verbindungsCodesDatenbank:
        print("bestätigt")
        return JsonResponse({"bestätigt": True})
    else:
        print("nicht bestätigt")
        return JsonResponse({"bestätigt": False})
