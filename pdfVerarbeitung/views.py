from django.shortcuts import render
from .forms import UnterschriftFormular
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import base64


def unterschriftView(request):
   

    if request.method == "POST":
        unterschriftFormular = UnterschriftFormular(request.POST)
        if unterschriftFormular.is_valid():
            verbindungsCode = request.POST.get("verbindungsCode")
            print(verbindungsCode)

            canvas_data = request.POST.get("canvasData")
            canvas_data = canvas_data.replace("data:image/png;base64,", "")
            binary_data = base64.b64decode(canvas_data)

            request.session["verbindungsCodeEingabe"] = verbindungsCode

            bildPfad = "unterschrift.png"
            with open(bildPfad, "wb") as fh:
                fh.write(binary_data)


    else:
        unterschriftFormular = UnterschriftFormular()

    return render(request, "unterschrift.html", {"unterschriftFormular": unterschriftFormular})


def unterschriftsBestaetigungView(request):
    verbindungsCodeErstellt = request.session.get("verbindungsCodeErstellt")
    verbindungsCodeEingabe = request.session.get("verbindungsCodeEingabe")

    print(verbindungsCodeErstellt, "verbindungsCodeErstellt", verbindungsCodeEingabe, "verbindungsCodeEingabe")

    if verbindungsCodeErstellt == verbindungsCodeEingabe and verbindungsCodeErstellt != None:
        codeBestaetigung = True

    else:
        codeBestaetigung = False

    return JsonResponse({"codeBestaetigung": codeBestaetigung})

