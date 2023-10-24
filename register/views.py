import datetime

from django.shortcuts import render
from .forms import kundenDatenForm
from pdfVerarbeitung.pdfFunktionen import verzeichnissErstellen
from pdfVerarbeitung.pdfScript import Datenschutz, Patientenerklärung, \
    Mehrkostenerklärung
from pdfVerarbeitung.models import PdfInformationDatenschutz, \
    PdfInformationPatientenerklärung, PdfInformationHöherwerigeversorgung


def register(request):
    if request.method == "POST":
        print("Post")

        formularKundendaten = kundenDatenForm(request.POST)
        pdfFormularDatenschutz = PdfInformationDatenschutz(request.POST)
        pdfFormularPatientenerklärung = PdfInformationPatientenerklärung(request.POST)
        pdfFormularHöherwerigeversorgung = PdfInformationHöherwerigeversorgung(request.POST)

        if formularKundendaten.is_valid():
            kunde = formularKundendaten.save()

            datumHeute = datetime.date.today().strftime("%d.%m.%Y")

            if pdfFormularDatenschutz.is_valid():
                Datenschutz.pdfFunktionenAufrufen(pdfFormularDatenschutz.cleaned_data, kunde)
                Datenschutz.personen_daten(kunde, datumHeute)

            if pdfFormularPatientenerklärung.is_valid():
                Patientenerklärung.pdfFunktionenAufrufen(pdfFormularPatientenerklärung.cleaned_data, kunde)
                Patientenerklärung.personen_daten(kunde, datumHeute)

            if pdfFormularHöherwerigeversorgung.is_valid():
                Mehrkostenerklärung.pdfFunktionenAufrufen(pdfFormularHöherwerigeversorgung.cleaned_data, kunde)

            _, kommpletteWegZumKundenverzeichnis, _ = verzeichnissErstellen(kunde, "pdfVerarbeitung/kundenunterlagen/")



    else:
        formularKundendaten = kundenDatenForm()

        pdfFormularDatenschutz = PdfInformationDatenschutz()
        pdfFormularPatientenerklärung = PdfInformationPatientenerklärung()
        pdfFormularHöherwerigeversorgung = PdfInformationHöherwerigeversorgung()

    return render(request, 'indexRegister.html',
                  {
                      "formularKundendaten": formularKundendaten,
                      "pdfFormularDatenschutz": pdfFormularDatenschutz,
                      "pdfFormularPatientenerklärung": pdfFormularPatientenerklärung,
                      "pdfFormularHöherwerigeversorgung": pdfFormularHöherwerigeversorgung})
