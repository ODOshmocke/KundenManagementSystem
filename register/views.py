from django.shortcuts import render
from .forms import UserInformationForm
from pdfVerarbeitung.models import PdfInformationDatenschutz, PdfInformationPatientenerklärung, \
    PdfInformationHöherwerigeversorgung


# Create your views here.
def pdfFunktionen(funktion):
    patientenerklärungFunktionen = {
        "daten_des___der_versicherten": PdfInformationPatientenerklärung.daten_des___der_versicherten,
        "ich_noch_keine_orthopaedischen_schuhzurichtungenerhalten_habe_erstmalige_versorgung": PdfInformationPatientenerklärung.ich_noch_keine_orthopaedischen_schuhzurichtungenerhalten_habe_erstmalige_versorgung,
        "ich__im__rahmen__der__erstmaligen__versorgung__erst__1__paar__orthopaedische__schuhzurichtungen_erhalten_habe": PdfInformationPatientenerklärung.ich__im__rahmen__der__erstmaligen__versorgung__erst__1__paar__orthopaedische__schuhzurichtungen_erhalten_habe,
        "ichim__rahmen__der__erstmaligen__versorgung__erst__2__paar__orthopaedische__schuhzurichtungen_erhalten_habe": PdfInformationPatientenerklärung.ichim__rahmen__der__erstmaligen__versorgung__erst__2__paar__orthopaedische__schuhzurichtungen_erhalten_habe,
        "ich__in__den__vergangenen__6__monaten__noch__keine__weitere__orthopaedische__schuhzurichtung_erhalten_habe": PdfInformationPatientenerklärung.ich__in__den__vergangenen__6__monaten__noch__keine__weitere__orthopaedische__schuhzurichtung_erhalten_habe,
        "ich_noch_keine_einlagen_erhalten_habeerstmalige_versorgung": PdfInformationPatientenerklärung.ich_noch_keine_einlagen_erhalten_habeerstmalige_versorgung,
        "ich__im__rahmen__der__erstmaligen__versorgung__erst__1__paar__einlagen__erhalten__habe__welche_ausreichend_mit_positivem_ergebnis_erprobt_wurden_wechselpaar": PdfInformationPatientenerklärung.ich__im__rahmen__der__erstmaligen__versorgung__erst__1__paar__einlagen__erhalten__habe__welche_ausreichend_mit_positivem_ergebnis_erprobt_wurden_wechselpaar,
        "ich_innerhalb_der_letzten_12_monate": PdfInformationPatientenerklärung.ich_innerhalb_der_letzten_12_monate,
        "keine_einlagen_oder": PdfInformationPatientenerklärung.keine_einlagen_oder,
        "erst_ein_paar_einlagenerhalten_habe": PdfInformationPatientenerklärung.erst_ein_paar_einlagenerhalten_habe,
        "dass_ich_nicht_mit_orthopaedischen_schuhenversorgt_wurde": PdfInformationPatientenerklärung.dass_ich_nicht_mit_orthopaedischen_schuhenversorgt_wurde,
        "datum_stempel_text": PdfInformationPatientenerklärung.datum_stempel_text
    }
    datenschutzFunktionen = {
        "personen_daten": PdfInformationDatenschutz.personen_daten,
        "gegenstand_der_verordnung_einlagen": PdfInformationDatenschutz.gegenstand_der_verordnung_einlagen,
        "gegenstand_der_verordnung_zurichtung": PdfInformationDatenschutz.gegenstand_der_verordnung_zurichtung,
        "gegenstand_der_verordnung_os": PdfInformationDatenschutz.gegenstand_der_verordnung_os,
        "sonstiges": PdfInformationDatenschutz.sonstiges,
        "werbung_ja": PdfInformationDatenschutz.werbung_ja,
        "werbung_nein": PdfInformationDatenschutz.werbung_nein
    }
    mehrkostenerklärungFunktionen = {
        "ich_habe_mich_fuer_eine_versorgung_mit_aufzahlung__mehrkosten__entschieden": PdfInformationHöherwerigeversorgung.ich_habe_mich_fuer_eine_versorgung_mit_aufzahlung__mehrkosten__entschieden,
        "ich_habe_mich_fuer_folgende_versorgung_entschieden": PdfInformationHöherwerigeversorgung.ich_habe_mich_fuer_folgende_versorgung_entschieden,
        "datum_stempel_text": PdfInformationHöherwerigeversorgung.datum_stempel_text
    }

    if funktion in patientenerklärungFunktionen:
         patientenerklärungFunktionen[funktion]()
    elif funktion in datenschutzFunktionen:
         datenschutzFunktionen[funktion]()
    elif funktion in mehrkostenerklärungFunktionen:
         mehrkostenerklärungFunktionen[funktion]()



def register(request):
    print(request.POST)

    if request.method == "POST":
        print("Post")

        formularKundendaten = UserInformationForm(request.POST)

        pdfFormularDatenschutz = PdfInformationDatenschutz(request.POST)
        pdfFormularPatientenerklärung = PdfInformationPatientenerklärung(request.POST)
        pdfFormularHöherwerigeversorgung = PdfInformationHöherwerigeversorgung(request.POST)

        if pdfFormularDatenschutz.is_valid():
            print(pdfFormularDatenschutz.cleaned_data)
        if pdfFormularPatientenerklärung.is_valid():
            print(pdfFormularPatientenerklärung.cleaned_data)
        if pdfFormularHöherwerigeversorgung.is_valid():
            print(pdfFormularHöherwerigeversorgung.cleaned_data)

        #print(pdfFormularHöherwerigeversorgung.cleaned_data, "pdfFormularHöherwerigeversorgung\n", pdfFormularPatientenerklärung.cleaned_data, "pdfFormularPatientenerklärung\n", pdfFormularDatenschutz.cleaned_data, "pdfFormularDatenschutz\n",)

        if formularKundendaten.is_valid():
            formularKundendaten.save()


    else:
        formularKundendaten = UserInformationForm()

        pdfFormularDatenschutz = PdfInformationDatenschutz()
        pdfFormularPatientenerklärung = PdfInformationPatientenerklärung()
        pdfFormularHöherwerigeversorgung = PdfInformationHöherwerigeversorgung()


    return render(request, 'indexRegister.html', {"formularKundendaten": formularKundendaten, "pdfFormularDatenschutz": pdfFormularDatenschutz, "pdfFormularPatientenerklärung": pdfFormularPatientenerklärung, "pdfFormularHöherwerigeversorgung": pdfFormularHöherwerigeversorgung})
