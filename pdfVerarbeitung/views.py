from django.shortcuts import render
from .forms import UnterschriftFormular
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def unterschriftView(request):
    if request.method == "POST":
        unterschriftFormular = UnterschriftFormular(request.POST)
        if unterschriftFormular.is_valid():
            print(unterschriftFormular.cleaned_data)
    else:
        unterschriftFormular = UnterschriftFormular()
    return render(request, "unterschrift.html", {"unterschriftFormular": unterschriftFormular})