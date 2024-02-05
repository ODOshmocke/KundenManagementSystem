import fitz
from pdfVerarbeitung.pdfFunktionen import verzeichnissErstellen, verzeichnissNamenErstellen
import os


# PDF-Datei öffnen

def pdfÖffnen(kunde):
    _, pfadKundenordner, verzeichnissExistiert = verzeichnissErstellen(kunde, "pdfVerarbeitung/kundenunterlagen/")
    if os.path.exists(pfadKundenordner + "/Mehrkostenerklärung.pdf"):
        pdf = fitz.open(pfadKundenordner + "/Mehrkostenerklärung.pdf")
    else:
        pdf = fitz.open('pdfVerarbeitung/pdfVorlagen/Mehrkostenerklärung.pdf')
    seite = pdf[0]

    return seite, pdf, pfadKundenordner


dateiSpeichern = 'tempPdf'
hoehe = 9
breite = 9


def ich_habe_mich_fuer_eine_versorgung_mit_aufzahlung__mehrkosten__entschieden(kunde):
    seite, pdf, pfadKundenordner = pdfÖffnen(kunde)
    y_kreuz = 167
    x_kreuz_mehrkosten = 63

    seite.draw_line(fitz.Point(x_kreuz_mehrkosten, y_kreuz), fitz.Point(x_kreuz_mehrkosten + breite, y_kreuz + hoehe))
    seite.draw_line(fitz.Point(x_kreuz_mehrkosten, y_kreuz + hoehe), fitz.Point(x_kreuz_mehrkosten + breite, y_kreuz))
    pdfSpeichern(pdf, pfadKundenordner)


def ich_habe_mich_fuer_folgende_versorgung_entschieden(kunde, versorgung_Text=''):
    seite, pdf, pfadKundenordner = pdfÖffnen(kunde)

    y_zeile1 = 245
    y_zeile2 = 280

    x_text = 85

    geteilter_index = versorgung_Text.rfind(" ", 0, 90)


    if len(versorgung_Text) <= 90:
        seite.insert_text((x_text, y_zeile1), versorgung_Text, fontsize=10, rotate=0, color=(0, 0, 0), overlay=True)
    else:
        seite.insert_text((x_text, y_zeile1), versorgung_Text[:geteilter_index], fontsize=10, rotate=0, color=(0, 0, 0),
                          overlay=True)
        seite.insert_text((x_text, y_zeile2), versorgung_Text[geteilter_index + 1:], fontsize=10, rotate=0,
                          color=(0, 0, 0), overlay=True)
    pdfSpeichern(pdf, pfadKundenordner)


def datum_stempel_text(kunde, datumHeute, text_stempelName, text_stempelAdresse):
    text_datum = str(datumHeute)
    seite, pdf, pfadKundenordner = pdfÖffnen(kunde)

    y_datum_und_stempel = 496
    y_stempelAdresse = 484
    y_unterschrift = 440
    x_datum = 87
    x_unterschrift = 165
    x_stempel = 350

    seite.insert_text((x_datum, y_datum_und_stempel), text_datum, fontsize=10, rotate=0, color=(0, 0, 0), overlay=True)

    seite.insert_text((x_stempel, y_stempelAdresse), text_stempelAdresse, fontsize=10, rotate=0, color=(0, 0, 0), overlay=True)
    seite.insert_text((x_stempel, y_datum_und_stempel), text_stempelName, fontsize=10, rotate=0, color=(0, 0, 0),
                      overlay=True)

    unterschriftPfad = f"pdfVerarbeitung/kundenunterlagen/{verzeichnissNamenErstellen(kunde)}/unterschrift.png"

    if os.path.exists(unterschriftPfad):
        print("Unterschrift gefunden in " + unterschriftPfad)
        bild = open(unterschriftPfad, "rb").read()
        seite.insert_image(fitz.Rect(x_unterschrift, y_unterschrift, x_unterschrift + 100, y_unterschrift + 50), stream=bild, overlay=True, rotate=90)
    else:
        print("Unterschrift nicht gefunden in " + unterschriftPfad)


    pdfSpeichern(pdf, pfadKundenordner)


# ich_habe_mich_fuer_folgende_versorgung_entschieden("Test")
# ich_habe_mich_fuer_eine_versorgung_mit_aufzahlung__mehrkosten__entschieden("Test")
# datum_stempel_text("Test", "Test", "Test")


def pdfFunktionenAufrufen(pdfFunktionen, kunde):


    mehrkostenerklärungFunktionen = {
        "ich_habe_mich_fuer_eine_versorgung_mit_aufzahlung_mehrkosten_entschieden_model": ich_habe_mich_fuer_eine_versorgung_mit_aufzahlung__mehrkosten__entschieden,
        "ich_habe_mich_fuer_folgende_versorgung_entschieden_model": ich_habe_mich_fuer_folgende_versorgung_entschieden,
        # "datum_stempel_text_model": datum_stempel_text
    }

    for funktion, parameter in pdfFunktionen.items():
        if funktion in mehrkostenerklärungFunktionen:
            if parameter is True or parameter is False or parameter is None or parameter == "":
                mehrkostenerklärungFunktionen[funktion](kunde)
            else:
                mehrkostenerklärungFunktionen[funktion](kunde, parameter)


def pdfSpeichern(pdf, pfadKundenordner):
    try:
        #        pdf.save(pfadKundenordner + "/Mehrkostenerklärung.pdf")

        pdf.save(pfadKundenordner + "/Mehrkostenerklärung.pdf")
    except:
        pdf.save(f"{pfadKundenordner}/Mehrkostenerklärung.pdf", incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP)
    pdf.close()
