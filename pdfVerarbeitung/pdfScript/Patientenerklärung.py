import fitz
import os
# PDF-Datei öffnen

if os.path.exists('../PDFTester/tempPDF/Patientenerklärung.pdf'):
    pdf = fitz.open('pdfVorlagen/Patientenerklärung.pdf')
else:
    pdf = fitz.open('pdfVorlagen/Patientenerklärung.pdf')

# Seite auswählen
seite = pdf[0]

dateiSpeichern = 'tempPDF'


hoehe = 6
breite = 6

text_vorname = "Max"
text_nachname = "Muster"
text_adresse = "Musterstrasse 1"
text_ort_plz = "8000 Zürich"
text_geburtsdatum = "01.01.1990"
text_kv_nummer = "1234567890"
text_verordnung = "Jens Muster"

x_daten = 200
x_einlagen = 284
x_kreuz_normal = 70


def daten_des___der_versicherten(text_vorname, text_nachname, text_adresse, text_ort_plz, text_geburtsdatum,
                                 text_kv_nummer, text_verordnung):
    y_name = 100
    y_adresse = 122
    y_ort_plz = 143
    y_geburtsdatum = 165
    y_kv_nummer = 187
    y_verordnung = 213

    x_daten = 200

    seite.insert_text((x_daten, y_name), text_vorname, fontsize=10, rotate=0, color=(0, 0, 0), overlay=True)
    seite.insert_text((x_daten + 140, y_name), text_nachname, fontsize=10, rotate=0, color=(0, 0, 0), overlay=True)
    seite.insert_text((x_daten, y_adresse), text_adresse, fontsize=10, rotate=0, color=(0, 0, 0), overlay=True)
    seite.insert_text((x_daten, y_ort_plz), text_ort_plz, fontsize=10, rotate=0, color=(0, 0, 0), overlay=True)
    seite.insert_text((x_daten, y_geburtsdatum), text_geburtsdatum, fontsize=10, rotate=0, color=(0, 0, 0),
                      overlay=True)
    seite.insert_text((x_daten, y_kv_nummer), text_kv_nummer, fontsize=10, rotate=0, color=(0, 0, 0), overlay=True)
    seite.insert_text((x_daten, y_verordnung), text_verordnung, fontsize=10, rotate=0, color=(0, 0, 0), overlay=True)


def ich_noch_keine_orthopaedischen_schuhzurichtungenerhalten_habe_erstmalige_versorgung():
    y_kreuz_1 = 311

    seite.draw_line(fitz.Point(x_kreuz_normal, y_kreuz_1), fitz.Point(x_kreuz_normal + breite, y_kreuz_1 + hoehe))
    seite.draw_line(fitz.Point(x_kreuz_normal, y_kreuz_1 + hoehe), fitz.Point(x_kreuz_normal + breite, y_kreuz_1))


def ich__im__rahmen__der__erstmaligen__versorgung__erst__1__paar__orthopaedische__schuhzurichtungen_erhalten_habe():
    y_kreuz_2 = 337

    seite.draw_line(fitz.Point(x_kreuz_normal, y_kreuz_2), fitz.Point(x_kreuz_normal + breite, y_kreuz_2 + hoehe))
    seite.draw_line(fitz.Point(x_kreuz_normal, y_kreuz_2 + hoehe), fitz.Point(x_kreuz_normal + breite, y_kreuz_2))


def ichim__rahmen__der__erstmaligen__versorgung__erst__2__paar__orthopaedische__schuhzurichtungen_erhalten_habe():
    y_kreuz_3 = 382.5

    seite.draw_line(fitz.Point(x_kreuz_normal, y_kreuz_3), fitz.Point(x_kreuz_normal + breite, y_kreuz_3 + hoehe))
    seite.draw_line(fitz.Point(x_kreuz_normal, y_kreuz_3 + hoehe), fitz.Point(x_kreuz_normal + breite, y_kreuz_3))


def ich__in__den__vergangenen__6__monaten__noch__keine__weitere__orthopaedische__schuhzurichtung_erhalten_habe():
    y_kreuz_4 = 425

    seite.draw_line(fitz.Point(x_kreuz_normal, y_kreuz_4), fitz.Point(x_kreuz_normal + breite, y_kreuz_4 + hoehe))
    seite.draw_line(fitz.Point(x_kreuz_normal, y_kreuz_4 + hoehe), fitz.Point(x_kreuz_normal + breite, y_kreuz_4))


def ich_noch_keine_einlagen_erhalten_habeerstmalige_versorgung():
    y_kreuz_5 = 502

    seite.draw_line(fitz.Point(x_kreuz_normal, y_kreuz_5), fitz.Point(x_kreuz_normal + breite, y_kreuz_5 + hoehe))
    seite.draw_line(fitz.Point(x_kreuz_normal, y_kreuz_5 + hoehe), fitz.Point(x_kreuz_normal + breite, y_kreuz_5))


def ich__im__rahmen__der__erstmaligen__versorgung__erst__1__paar__einlagen__erhalten__habe__welche_ausreichend_mit_positivem_ergebnis_erprobt_wurden_wechselpaar():
    y_kreuz_6 = 534

    seite.draw_line(fitz.Point(x_kreuz_normal, y_kreuz_6), fitz.Point(x_kreuz_normal + breite, y_kreuz_6 + hoehe))
    seite.draw_line(fitz.Point(x_kreuz_normal, y_kreuz_6 + hoehe), fitz.Point(x_kreuz_normal + breite, y_kreuz_6))


def ich_innerhalb_der_letzten_12_monate():
    y_kreuz_7 = 574

    seite.draw_line(fitz.Point(x_kreuz_normal, y_kreuz_7), fitz.Point(x_kreuz_normal + breite, y_kreuz_7 + hoehe))
    seite.draw_line(fitz.Point(x_kreuz_normal, y_kreuz_7 + hoehe), fitz.Point(x_kreuz_normal + breite, y_kreuz_7))


def keine_einlagen_oder():
    y_kreuz_8 = 574

    seite.draw_line(fitz.Point(x_einlagen, y_kreuz_8), fitz.Point(x_einlagen + breite, y_kreuz_8 + hoehe))
    seite.draw_line(fitz.Point(x_einlagen, y_kreuz_8 + hoehe), fitz.Point(x_einlagen + breite, y_kreuz_8))


def erst_ein_paar_einlagenerhalten_habe():
    y_kreuz_9 = 598

    seite.draw_line(fitz.Point(x_einlagen, y_kreuz_9), fitz.Point(x_einlagen + breite, y_kreuz_9 + hoehe))
    seite.draw_line(fitz.Point(x_einlagen, y_kreuz_9 + hoehe), fitz.Point(x_einlagen + breite, y_kreuz_9))


def dass_ich_nicht_mit_orthopaedischen_schuhenversorgt_wurde():
    y_kreuz_10 = 641

    seite.draw_line(fitz.Point(x_kreuz_normal, y_kreuz_10), fitz.Point(x_kreuz_normal + breite, y_kreuz_10 + hoehe))
    seite.draw_line(fitz.Point(x_kreuz_normal, y_kreuz_10 + hoehe), fitz.Point(x_kreuz_normal + breite, y_kreuz_10))


def datum_stempel_text(text_datum, text_stempel):
    y_datum = 782
    x_datum = 87
    x_stempel = 350

    seite.insert_text((x_datum, y_datum), text_datum, fontsize=10, rotate=0, color=(0, 0, 0), overlay=True)
    seite.insert_text((x_stempel, y_datum), text_stempel, fontsize=10, rotate=0, color=(0, 0, 0), overlay=True)

datum_stempel_text("01.01.2021", "Stempel")


try:
    pdf.save(f"{dateiSpeichern}/Patientenerklärung.pdf")
except Exception as e:
    pdf.save(f"{dateiSpeichern}/Patientenerklärung.pdf", incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP)
pdf.close()




