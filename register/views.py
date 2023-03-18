from django.shortcuts import render
from .forms import UserInformationForm
# Create your views here.


def register(request):


    if request.method == "POST":
        print("Post")
        form = UserInformationForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            print("Form is valid")


    else:
        form = UserInformationForm()
        print("Else")


    return render(request, 'indexRegister.html', {"form": form})



