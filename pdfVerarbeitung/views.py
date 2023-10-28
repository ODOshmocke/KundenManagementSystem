from django.shortcuts import render
from .forms import UnterschriftFormular
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import base64

@csrf_exempt
def unterschriftView(request):
    if request.method == "POST":
        unterschriftFormular = UnterschriftFormular(request.POST)
        if unterschriftFormular.is_valid():
            canvas_data = request.POST.get("canvasData")
            canvas_data = canvas_data.replace("data:image/png;base64,", "")
            binary_data = base64.b64decode(canvas_data)

            bildPfad = "unterschrift.png"
            with open(bildPfad, "wb") as fh:
                fh.write(binary_data)


    else:
        unterschriftFormular = UnterschriftFormular()
    return render(request, "unterschrift.html", {"unterschriftFormular": unterschriftFormular})