import fitz
from pdfVerarbeitung.pdfFunktionen import verzeichnissErstellen,  verzeichnissNamenErstellen
import os
# PDF-Datei öffnen

def pdfÖffnen(kunde):
    _, pfadKundenordner, _ = verzeichnissErstellen(kunde, "pdfVerarbeitung/kundenunterlagen/")

    if os.path.exists(pfadKundenordner + "/Datenschutz.pdf"):
        pdf = fitz.open(pfadKundenordner + "/Datenschutz.pdf")
    else:
        pdf = fitz.open('pdfVerarbeitung/pdfVorlagen/Datenschutz.pdf')
    seite = pdf[0]

    return seite, pdf, pfadKundenordner


y_kreuz_werbung = 570
y_kreuz_verordnung = 305

breite = 10  # Breite des Rechtecks
hoehe = 10  # Höhe des Rechtecks


def personen_daten(kunde, datumHeute, ortHeute=''):
    seite, pdf, pfadKundenordner = pdfÖffnen(kunde)

    text_name = kunde.vorname + " " + kunde.nachname
    text_geburtsdatum = str(kunde.geburtsdatum)
    text_adresse = kunde.strasse + " " + kunde.ort_plz
    text_email = kunde.email
    text_kv_nummer = kunde.kv_nummer
    text_datum = str(datumHeute)
    text_ort = str(ortHeute)


    y_name = 149  # y-Koordinate
    y_geburtsdatum = 180
    y_adresse = 205  # y-Koordinate
    y_email = 253
    y_medizinische_verordnung = 277
    y_kv_nummer = 373
    y_datum = 798
    x_name = 110  # x-Koordinate
    x_text = 290  # x-Koordinate
    x_datum = 70
    x_unterschrift = 100
    y_unterschrift = 730
    x_ort = 290
    y_ort = 750

    seite.insert_text((x_name, y_name), text_name, fontsize=10, rotate=0, color=(0, 0, 0), overlay=True)
    seite.insert_text((x_text, y_geburtsdatum), text_geburtsdatum, fontsize=10, rotate=0, color=(0, 0, 0), overlay=True)
    seite.insert_text((x_text, y_adresse), text_adresse, fontsize=10, rotate=0, color=(0, 0, 0), overlay=True)
    seite.insert_text((x_text, y_email), text_email, fontsize=10, rotate=0, color=(0, 0, 0), overlay=True)
    seite.insert_text((x_text, y_kv_nummer), text_kv_nummer, fontsize=10, rotate=0, color=(0, 0, 0), overlay=True)
    #seite.insert_text((x_ort, y_ort), text_ort, fontsize=10, rotate=0, color=(0, 0, 0), overlay=True)

    unterschriftPfad = f"pdfVerarbeitung/kundenunterlagen/{verzeichnissNamenErstellen(kunde)}/unterschrift.png"

    if os.path.exists(unterschriftPfad):
        print("Unterschrift gefunden in " + unterschriftPfad)
        bild = open(unterschriftPfad, "rb").read()
        seite.insert_image(fitz.Rect(x_unterschrift, y_unterschrift, x_unterschrift + 100, y_unterschrift + 50), stream=bild, overlay=True, rotate=90)
    else:
        print("Unterschrift nicht gefunden in " + unterschriftPfad)
    seite.insert_text((x_datum, y_datum), text_datum, fontsize=10, rotate=0, color=(0, 0, 0), overlay=True)

    pdfSpeichern(pdf, pfadKundenordner)


def medizinische_verordnung(kunde, text_medizinische_verordnung=''):
    seite, pdf, pfadKundenordner = pdfÖffnen(kunde)
    x_medizinische_verordnung = 290
    y_medizinische_verordnung = 277
    seite.insert_text((x_medizinische_verordnung, y_medizinische_verordnung), text_medizinische_verordnung, fontsize=10,
                      rotate=0, color=(0, 0, 0), overlay=True)
    pdfSpeichern(pdf, pfadKundenordner)

def gegenstand_der_verordnung_einlagen(kunde):
    seite, pdf, pfadKundenordner = pdfÖffnen(kunde)
    x_kreuz_einlagen = 340

    seite.draw_line(fitz.Point(x_kreuz_einlagen, y_kreuz_verordnung),
                    fitz.Point(x_kreuz_einlagen + breite, y_kreuz_verordnung + hoehe))
    seite.draw_line(fitz.Point(x_kreuz_einlagen, y_kreuz_verordnung + hoehe),
                    fitz.Point(x_kreuz_einlagen + breite, y_kreuz_verordnung))
    pdfSpeichern(pdf, pfadKundenordner)



def gegenstand_der_verordnung_zurichtung(kunde):
    seite, pdf, pfadKundenordner = pdfÖffnen(kunde)
    x_kreuz_zurichtung = 428

    seite.draw_line(fitz.Point(x_kreuz_zurichtung, y_kreuz_verordnung),
                    fitz.Point(x_kreuz_zurichtung + breite, y_kreuz_verordnung + hoehe))
    seite.draw_line(fitz.Point(x_kreuz_zurichtung, y_kreuz_verordnung + hoehe),
                    fitz.Point(x_kreuz_zurichtung + breite, y_kreuz_verordnung))
    pdfSpeichern(pdf, pfadKundenordner)



def gegenstand_der_verordnung_os(kunde):
    seite, pdf, pfadKundenordner = pdfÖffnen(kunde)
    x_kreuz_os = 484

    seite.draw_line(fitz.Point(x_kreuz_os, y_kreuz_verordnung),
                    fitz.Point(x_kreuz_os + breite, y_kreuz_verordnung + hoehe))
    seite.draw_line(fitz.Point(x_kreuz_os, y_kreuz_verordnung + hoehe),
                    fitz.Point(x_kreuz_os + breite, y_kreuz_verordnung))
    pdfSpeichern(pdf, pfadKundenordner)



def sonstiges(kunde, text_sonstiges=''):
    seite, pdf, pfadKundenordner = pdfÖffnen(kunde)
    x_sonstiges = 350
    y_sonstiges = 337
    seite.insert_text((x_sonstiges, y_sonstiges), text_sonstiges, fontsize=10, rotate=0, color=(0, 0, 0), overlay=True)
    pdfSpeichern(pdf, pfadKundenordner)



def werbung_ja(kunde):
    seite, pdf, pfadKundenordner = pdfÖffnen(kunde)
    x_kreuz_werbung_ja = 398
    seite.draw_line(fitz.Point(x_kreuz_werbung_ja, y_kreuz_werbung),
                    fitz.Point(x_kreuz_werbung_ja + breite, y_kreuz_werbung + hoehe))
    seite.draw_line(fitz.Point(x_kreuz_werbung_ja, y_kreuz_werbung + hoehe),
                    fitz.Point(x_kreuz_werbung_ja + breite, y_kreuz_werbung))
    pdfSpeichern(pdf, pfadKundenordner)



def werbung_nein(kunde):
    seite, pdf, pfadKundenordner = pdfÖffnen(kunde)
    x_kreuz_werbung_nein = 180
    seite.draw_line(fitz.Point(x_kreuz_werbung_nein, y_kreuz_werbung),
                    fitz.Point(x_kreuz_werbung_nein + breite, y_kreuz_werbung + hoehe))
    seite.draw_line(fitz.Point(x_kreuz_werbung_nein, y_kreuz_werbung + hoehe),
                    fitz.Point(x_kreuz_werbung_nein + breite, y_kreuz_werbung))
    pdfSpeichern(pdf, pfadKundenordner)


def pdfFunktionenAufrufen(pdfFunktionen, kunde):


    datenschutzFunktionen = {
        #"personen_daten_model": personen_daten,
        "medizinische_verordnung_model": medizinische_verordnung,
        "gegenstand_der_verordnung_einlagen_model": gegenstand_der_verordnung_einlagen,
        "gegenstand_der_verordnung_zurichtung_model": gegenstand_der_verordnung_zurichtung,
        "gegenstand_der_verordnung_os_model": gegenstand_der_verordnung_os,
        "sonstiges_model": sonstiges,
        "werbung_ja_model": werbung_ja,
        "werbung_nein_model": werbung_nein
    }

    for funktion, parameter in pdfFunktionen.items():

        if funktion in datenschutzFunktionen:
            if parameter is True or parameter is False or parameter is None or parameter == "":
                datenschutzFunktionen[funktion](kunde)
            else:
                datenschutzFunktionen[funktion](kunde, parameter)


def pdfSpeichern(pdf, pfadKundenordner):
    try:
        pdf.save(pfadKundenordner + "/Datenschutz.pdf")
    except:
        pdf.save(pfadKundenordner + "/Datenschutz.pdf", incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP)
    pdf.close()

