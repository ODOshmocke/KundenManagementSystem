import fitz
import os
# PDF-Datei öffnen

if os.path.exists('../PDFTester/tempPDF/Patientenerklärung.pdf'):
    pdf = fitz.open('pdfVorlagen/Mehrkostenerklärung.pdf')
else:
    pdf = fitz.open('pdfVorlagen/Mehrkostenerklärung.pdf')

# Seite auswählen
seite = pdf[0]


dateiSpeichern = 'tempPDF'
hoehe = 9
breite = 9



def ich_habe_mich_fuer_eine_versorgung_mit_aufzahlung__mehrkosten__entschieden():
    y_kreuz = 167
    x_kreuz_mehrkosten = 63

    seite.draw_line(fitz.Point(x_kreuz_mehrkosten, y_kreuz), fitz.Point(x_kreuz_mehrkosten + breite, y_kreuz + hoehe))
    seite.draw_line(fitz.Point(x_kreuz_mehrkosten, y_kreuz + hoehe), fitz.Point(x_kreuz_mehrkosten + breite, y_kreuz))


def ich_habe_mich_fuer_folgende_versorgung_entschieden(versorgung_Text):
    y_zeile1 = 245
    y_zeile2 = 280

    x_text = 85

    print(len(versorgung_Text))
    geteilter_index = versorgung_Text.rfind(" ", 0, 100)

    if geteilter_index == -1:
        seite.insert_text((x_text, y_zeile1), versorgung_Text, fontsize=11, rotate=0, color=(0, 0, 0), overlay=True)
    else:
        seite.insert_text((x_text, y_zeile1), versorgung_Text[:geteilter_index], fontsize=11, rotate=0, color=(0, 0, 0), overlay=True)
        seite.insert_text((x_text, y_zeile2), versorgung_Text[geteilter_index + 1:], fontsize=11, rotate=0, color=(0, 0, 0), overlay=True)




def datum_stempel_text(text_datum, text_stempel):
    y_datum_und_stempel = 496
    x_datum = 87
    x_stempel = 350

    seite.insert_text((x_datum, y_datum_und_stempel), text_datum, fontsize=10, rotate=0, color=(0, 0, 0), overlay=True)
    seite.insert_text((x_stempel, y_datum_und_stempel), text_stempel, fontsize=10, rotate=0, color=(0, 0, 0), overlay=True)


ich_habe_mich_fuer_eine_versorgung_mit_aufzahlung__mehrkosten__entschieden()
ich_habe_mich_fuer_folgende_versorgung_entschieden("including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do")
datum_stempel_text("01.01.2021", "Stempel")


try:
    pdf.save(f"{dateiSpeichern}/Mehrkostenerklärung.pdf")
except Exception as e:
    pdf.save(f"{dateiSpeichern}/Mehrkostenerklärung.pdf", incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP)
pdf.close()


