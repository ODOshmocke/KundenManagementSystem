from pdfVerarbeitung.pdfFunktionen import verzeichnissErstellen
import fitz
import os
# PDF-Datei öffnen

def pdfÖffnen(kunde):
    _, pfadKundenordner, verzeichnissExistiert = verzeichnissErstellen(kunde, "pdfVerarbeitung/kundenunterlagen/")
    if os.path.exists(pfadKundenordner + "/Patientenerklärung.pdf"):
        pdf = fitz.open(pfadKundenordner + "/Patientenerklärung.pdf")
    else:
        pdf = fitz.open('pdfVerarbeitung/pdfVorlagen/Patientenerklärung.pdf')
    seite = pdf[0]

    return seite, pdf, pfadKundenordner


# Seite auswählen

dateiSpeichern = 'tempPdf'


hoehe = 6
breite = 6



x_daten = 200
x_einlagen = 284
x_kreuz_normal = 70


def personen_daten(kunde, datumHeute):
    seite, pdf, pfadKundenordner = pdfÖffnen(kunde)

    text_name = kunde.vorname + " " + kunde.nachname
    text_geburtsdatum = str(kunde.geburtsdatum)
    text_adresse = kunde.strasse
    text_ort_plz = kunde.ort_plz
    text_kv_nummer = kunde.kv_nummer
    text_verordnung = str(datumHeute)

    y_name = 100
    y_adresse = 122
    y_ort_plz = 143
    y_geburtsdatum = 165
    y_kv_nummer = 187
    y_verordnung = 213

    x_daten = 200

    seite.insert_text((x_daten, y_name), text_name, fontsize=10, rotate=0, color=(0, 0, 0), overlay=True)
    seite.insert_text((x_daten, y_adresse), text_adresse, fontsize=10, rotate=0, color=(0, 0, 0), overlay=True)
    seite.insert_text((x_daten, y_ort_plz), text_ort_plz, fontsize=10, rotate=0, color=(0, 0, 0), overlay=True)
    seite.insert_text((x_daten, y_geburtsdatum), text_geburtsdatum, fontsize=10, rotate=0, color=(0, 0, 0),
                      overlay=True)
    seite.insert_text((x_daten, y_kv_nummer), text_kv_nummer, fontsize=10, rotate=0, color=(0, 0, 0), overlay=True)
    seite.insert_text((x_daten, y_verordnung), text_verordnung, fontsize=10, rotate=0, color=(0, 0, 0), overlay=True)
    pdfSpeichern(pdf, pfadKundenordner)


def ich_noch_keine_orthopaedischen_schuhzurichtungenerhalten_habe_erstmalige_versorgung(kunde):
    seite, pdf, pfadKundenordner = pdfÖffnen(kunde)

    y_kreuz_1 = 311

    seite.draw_line(fitz.Point(x_kreuz_normal, y_kreuz_1), fitz.Point(x_kreuz_normal + breite, y_kreuz_1 + hoehe))
    seite.draw_line(fitz.Point(x_kreuz_normal, y_kreuz_1 + hoehe), fitz.Point(x_kreuz_normal + breite, y_kreuz_1))
    pdfSpeichern(pdf, pfadKundenordner)


def ich__im__rahmen__der__erstmaligen__versorgung__erst__1__paar__orthopaedische__schuhzurichtungen_erhalten_habe(kunde):
    seite, pdf, pfadKundenordner = pdfÖffnen(kunde)

    y_kreuz_2 = 337

    seite.draw_line(fitz.Point(x_kreuz_normal, y_kreuz_2), fitz.Point(x_kreuz_normal + breite, y_kreuz_2 + hoehe))
    seite.draw_line(fitz.Point(x_kreuz_normal, y_kreuz_2 + hoehe), fitz.Point(x_kreuz_normal + breite, y_kreuz_2))
    pdfSpeichern(pdf, pfadKundenordner)


def ichim__rahmen__der__erstmaligen__versorgung__erst__2__paar__orthopaedische__schuhzurichtungen_erhalten_habe(kunde):
    seite, pdf, pfadKundenordner = pdfÖffnen(kunde)

    y_kreuz_3 = 382.5

    seite.draw_line(fitz.Point(x_kreuz_normal, y_kreuz_3), fitz.Point(x_kreuz_normal + breite, y_kreuz_3 + hoehe))
    seite.draw_line(fitz.Point(x_kreuz_normal, y_kreuz_3 + hoehe), fitz.Point(x_kreuz_normal + breite, y_kreuz_3))
    pdfSpeichern(pdf, pfadKundenordner)


def ich__in__den__vergangenen__6__monaten__noch__keine__weitere__orthopaedische__schuhzurichtung_erhalten_habe(kunde):
    seite, pdf, pfadKundenordner = pdfÖffnen(kunde)
    y_kreuz_4 = 425

    seite.draw_line(fitz.Point(x_kreuz_normal, y_kreuz_4), fitz.Point(x_kreuz_normal + breite, y_kreuz_4 + hoehe))
    seite.draw_line(fitz.Point(x_kreuz_normal, y_kreuz_4 + hoehe), fitz.Point(x_kreuz_normal + breite, y_kreuz_4))
    pdfSpeichern(pdf, pfadKundenordner)


def ich_noch_keine_einlagen_erhalten_habeerstmalige_versorgung(kunde):
    seite, pdf, pfadKundenordner = pdfÖffnen(kunde)

    y_kreuz_5 = 502

    seite.draw_line(fitz.Point(x_kreuz_normal, y_kreuz_5), fitz.Point(x_kreuz_normal + breite, y_kreuz_5 + hoehe))
    seite.draw_line(fitz.Point(x_kreuz_normal, y_kreuz_5 + hoehe), fitz.Point(x_kreuz_normal + breite, y_kreuz_5))
    pdfSpeichern(pdf, pfadKundenordner)


def ich__im__rahmen__der__erstmaligen__versorgung__erst__1__paar__einlagen__erhalten__habe__welche_ausreichend_mit_positivem_ergebnis_erprobt_wurden_wechselpaar(kunde):
    seite, pdf, pfadKundenordner = pdfÖffnen(kunde)

    y_kreuz_6 = 534

    seite.draw_line(fitz.Point(x_kreuz_normal, y_kreuz_6), fitz.Point(x_kreuz_normal + breite, y_kreuz_6 + hoehe))
    seite.draw_line(fitz.Point(x_kreuz_normal, y_kreuz_6 + hoehe), fitz.Point(x_kreuz_normal + breite, y_kreuz_6))
    pdfSpeichern(pdf, pfadKundenordner)


def ich_innerhalb_der_letzten_12_monate(kunde):
    seite, pdf, pfadKundenordner = pdfÖffnen(kunde)

    y_kreuz_7 = 574

    seite.draw_line(fitz.Point(x_kreuz_normal, y_kreuz_7), fitz.Point(x_kreuz_normal + breite, y_kreuz_7 + hoehe))
    seite.draw_line(fitz.Point(x_kreuz_normal, y_kreuz_7 + hoehe), fitz.Point(x_kreuz_normal + breite, y_kreuz_7))
    pdfSpeichern(pdf, pfadKundenordner)


def keine_einlagen_oder(kunde):
    seite, pdf, pfadKundenordner = pdfÖffnen(kunde)

    y_kreuz_8 = 574

    seite.draw_line(fitz.Point(x_einlagen, y_kreuz_8), fitz.Point(x_einlagen + breite, y_kreuz_8 + hoehe))
    seite.draw_line(fitz.Point(x_einlagen, y_kreuz_8 + hoehe), fitz.Point(x_einlagen + breite, y_kreuz_8))
    pdfSpeichern(pdf, pfadKundenordner)


def erst_ein_paar_einlagenerhalten_habe(kunde):
    seite, pdf, pfadKundenordner = pdfÖffnen(kunde)

    y_kreuz_9 = 598

    seite.draw_line(fitz.Point(x_einlagen, y_kreuz_9), fitz.Point(x_einlagen + breite, y_kreuz_9 + hoehe))
    seite.draw_line(fitz.Point(x_einlagen, y_kreuz_9 + hoehe), fitz.Point(x_einlagen + breite, y_kreuz_9))
    pdfSpeichern(pdf, pfadKundenordner)


def dass_ich_nicht_mit_orthopaedischen_schuhenversorgt_wurde(kunde):
    seite, pdf, pfadKundenordner = pdfÖffnen(kunde)

    y_kreuz_10 = 641

    seite.draw_line(fitz.Point(x_kreuz_normal, y_kreuz_10), fitz.Point(x_kreuz_normal + breite, y_kreuz_10 + hoehe))
    seite.draw_line(fitz.Point(x_kreuz_normal, y_kreuz_10 + hoehe), fitz.Point(x_kreuz_normal + breite, y_kreuz_10))
    pdfSpeichern(pdf, pfadKundenordner)


def datum_stempel_text(kunde, text_datum, text_stempel):
    seite, pdf, pfadKundenordner = pdfÖffnen(kunde)

    y_datum = 782
    x_datum = 87
    x_stempel = 350

    seite.insert_text((x_datum, y_datum), text_datum, fontsize=10, rotate=0, color=(0, 0, 0), overlay=True)
    seite.insert_text((x_stempel, y_datum), text_stempel, fontsize=10, rotate=0, color=(0, 0, 0), overlay=True)
    pdfSpeichern(pdf, pfadKundenordner)



def pdfFunktionenAufrufen(pdfFunktionen, kunde):
    patientenerklärungFunktionen = {
        #"daten_des___der_versicherten_model": daten_des___der_versicherten,
        "ich_noch_keine_orthopaedischen_schuhzurichtungenerhalten_habe_erstmalige_versorgung_model": ich_noch_keine_orthopaedischen_schuhzurichtungenerhalten_habe_erstmalige_versorgung,
        "ich__im__rahmen__der__erstmaligen__versorgung__erst__1__paar__orthopaedische__schuhzurichtungen_erhalten_habe_model": ich__im__rahmen__der__erstmaligen__versorgung__erst__1__paar__orthopaedische__schuhzurichtungen_erhalten_habe,
        "ich_im_rahmen_der_erstmaligen_versorgung_erst_2_paar_orthopaedische_schuhzurichtungen_erhalten_habe_model": ichim__rahmen__der__erstmaligen__versorgung__erst__2__paar__orthopaedische__schuhzurichtungen_erhalten_habe,
        "ich__in__den__vergangenen__6__monaten__noch__keine__weitere__orthopaedische__schuhzurichtung_erhalten_habe_model": ich__in__den__vergangenen__6__monaten__noch__keine__weitere__orthopaedische__schuhzurichtung_erhalten_habe,
        "ich_noch_keine_einlagen_erhalten_habeerstmalige_versorgung_model": ich_noch_keine_einlagen_erhalten_habeerstmalige_versorgung,
        "ich__im__rahmen__der__erstmaligen__versorgung__erst__1__paar__einlagen__erhalten__habe__welche_ausreichend_mit_positivem_ergebnis_erprobt_wurden_wechselpaar_model": ich__im__rahmen__der__erstmaligen__versorgung__erst__1__paar__einlagen__erhalten__habe__welche_ausreichend_mit_positivem_ergebnis_erprobt_wurden_wechselpaar,
        "ich_innerhalb_der_letzten_12_monate_model": ich_innerhalb_der_letzten_12_monate,
        "keine_einlagen_oder_model": keine_einlagen_oder,
        "erst_ein_paar_einlagenerhalten_habe_model": erst_ein_paar_einlagenerhalten_habe,
        "dass_ich_nicht_mit_orthopaedischen_schuhenversorgt_wurde_model": dass_ich_nicht_mit_orthopaedischen_schuhenversorgt_wurde,
        #"datum_stempel_text_model": datum_stempel_text
    }

    for funktion, parameter in pdfFunktionen.items():

        if funktion in patientenerklärungFunktionen:
            if parameter is True or parameter is False or parameter is None or parameter == "":
                patientenerklärungFunktionen[funktion](kunde)
            else:
                patientenerklärungFunktionen[funktion](kunde, parameter)


def pdfSpeichern(pdf, pfadKundenordner):
    try:
        pdf.save(f"{pfadKundenordner}/Patientenerklärung.pdf")
    except:
        pdf.save(f"{pfadKundenordner}/Patientenerklärung.pdf", incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP)
    pdf.close()






