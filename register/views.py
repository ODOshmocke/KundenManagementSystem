import datetime
import json
import random
import shutil
import urllib.parse

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
        shutil.copy(f"media/unterschriften/{verbindungsCode}_unterschrift.png",
                    f"pdfVerarbeitung/kundenunterlagen/{verzeichnissNamenErstellen(kunde)}/unterschrift.png")
    except:
        print("Unterschrift konnte nicht gefunden werden")


def register(request, kundenDaten=None, kundenDatenInitial=None):
    global encodedKundenDatenJson
    if kundenDaten != None:
        encodedKundenDaten = urllib.parse.parse_qs(kundenDaten)
        encodedKundenDatenJson = json.loads(json.dumps(encodedKundenDaten))  # in json umwandeln

        #remove list from dict
        for key in encodedKundenDatenJson:
            encodedKundenDatenJson[key] = encodedKundenDatenJson[key][0]

        if encodedKundenDatenJson["geschlecht"].lower() == "m":
            encodedKundenDatenJson["geschlecht"] = "Männlich"
        else:
            encodedKundenDatenJson["geschlecht"] = "Weiblich"

        kundenDatenInitial = {
            "vorname": encodedKundenDatenJson["vorname"],
            "nachname": encodedKundenDatenJson["nachname"],
            "strasse": encodedKundenDatenJson["strasse"],
            "ort_plz": encodedKundenDatenJson["ort_plz"],
            "krankenkasse": encodedKundenDatenJson["versicherungsname"],
            "geburtsdatum": encodedKundenDatenJson["geburtsdatum"],
            "geschlecht": encodedKundenDatenJson["geschlecht"],
            "kv_nummer": encodedKundenDatenJson["kv_nummer"],
        }
        print(encodedKundenDatenJson, "encodedKundenDaten")
        print(type(encodedKundenDatenJson), "type encodedKundenDaten")




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
            print("Verzeichniss wurde erstellt", kommpletteWegZumKundenverzeichnis)



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
        if kundenDatenInitial != None:
             formularKundendaten = kundenDatenForm(initial=kundenDatenInitial)
        else:
            formularKundendaten = kundenDatenForm()

        pdfFormularDatenschutz = PdfInformationDatenschutz()
        pdfFormularPatientenerklärung = PdfInformationPatientenerklärung()
        pdfFormularHöherwerigeversorgung = PdfInformationHöherwerigeversorgung()

    return render(request, 'indexRegister.html',
                  {
                      "formularKundendaten": formularKundendaten,
                      "verbindungsCode": verbindungsCodeErstellen(),
                      "pdfFormularDatenschutz": pdfFormularDatenschutz,
                      "pdfFormularPatientenerklärung": pdfFormularPatientenerklärung,
                      "pdfFormularHöherwerigeversorgung": pdfFormularHöherwerigeversorgung})
