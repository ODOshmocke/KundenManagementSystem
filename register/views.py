import datetime
import random
import shutil

from django.shortcuts import render
from .forms import kundenDatenForm
from .models import KundenDaten

from pdfVerarbeitung.pdfFunktionen import verzeichnissErstellen, verzeichnissNamenErstellen
from pdfVerarbeitung.pdfScript import Datenschutz, Patientenerklärung, \
    Mehrkostenerklärung
from pdfVerarbeitung.models import PdfInformationDatenschutz, \
    PdfInformationPatientenerklärung, PdfInformationHöherwerigeversorgung

def verbindungsCodeErstellen():
    ausgeschlosseneCodes = KundenDaten.objects.values_list("verbindungsCode", flat=True)
    verbindungsCodeErstellt = random.randint(1000, 9999)
    if verbindungsCodeErstellt in ausgeschlosseneCodes:
        verbindungsCodeErstellen()
    return verbindungsCodeErstellt
    


def unterschriftZumVerzeichnissHinzufügen(kunde):
    verbindungsCode = str(kunde.verbindungsCode)
    try:
        shutil.copy(f"media/unterschriften/{verbindungsCode}_unterschrift.png", f"pdfVerarbeitung/kundenunterlagen/{verzeichnissNamenErstellen(kunde)}/unterschrift.png")
    except:
        print("Unterschrift konnte nicht gefunden werden")




def register(request):

    if request.method == "POST":


        verbindungsCode = request.POST.get("verbindungsCode")


        formularKundendaten = kundenDatenForm(request.POST)
        pdfFormularDatenschutz = PdfInformationDatenschutz(request.POST)
        pdfFormularPatientenerklärung = PdfInformationPatientenerklärung(request.POST)
        pdfFormularHöherwerigeversorgung = PdfInformationHöherwerigeversorgung(request.POST)


        if formularKundendaten.is_valid():
            kunde = formularKundendaten.save(commit=False)
            kunde.verbindungsCode = verbindungsCode
            kunde.save()
            print("Kunde wurde gespeichert")

            _, kommpletteWegZumKundenverzeichnis, _ = verzeichnissErstellen(kunde, "pdfVerarbeitung/kundenunterlagen/")
            unterschriftZumVerzeichnissHinzufügen(kunde)


            datumHeute = datetime.date.today().strftime("%d.%m.%Y")

            if pdfFormularDatenschutz.is_valid():
                Datenschutz.pdfFunktionenAufrufen(pdfFormularDatenschutz.cleaned_data, kunde)
                Datenschutz.personen_daten(kunde, datumHeute)

            if pdfFormularPatientenerklärung.is_valid():
                Patientenerklärung.pdfFunktionenAufrufen(pdfFormularPatientenerklärung.cleaned_data, kunde)
                Patientenerklärung.personen_daten(kunde, datumHeute)

            if pdfFormularHöherwerigeversorgung.is_valid():
                Mehrkostenerklärung.pdfFunktionenAufrufen(pdfFormularHöherwerigeversorgung.cleaned_data, kunde)


    else:
        formularKundendaten = kundenDatenForm()

        pdfFormularDatenschutz = PdfInformationDatenschutz()
        pdfFormularPatientenerklärung = PdfInformationPatientenerklärung()
        pdfFormularHöherwerigeversorgung = PdfInformationHöherwerigeversorgung()

    return render(request, 'indexRegister.html',
                  {
                      "formularKundendaten": formularKundendaten,
                      "verbindungsCode":verbindungsCodeErstellen(),
                      "pdfFormularDatenschutz": pdfFormularDatenschutz,
                      "pdfFormularPatientenerklärung": pdfFormularPatientenerklärung,
                      "pdfFormularHöherwerigeversorgung": pdfFormularHöherwerigeversorgung})
