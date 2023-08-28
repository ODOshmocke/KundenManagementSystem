import fitz
import os
# PDF-Datei öffnen

if os.path.exists('/Datenschutz.pdf'):
    pdf = fitz.open('/Datenschutz.pdf')

else:
    pdf = fitz.open('Datenschutz.pdf')
# Seite auswählen
seite = pdf[0]

y_kreuz_werbung = 570
y_kreuz_verordnung = 305

breite = 10  # Breite des Rechtecks
hoehe = 10  # Höhe des Rechtecks


def personen_daten(text_name, text_geburtsdatum, text_adresse, text_email, text_medizinische_verordnung, text_kv_nummer,
                   text_datum):
    y_name = 149  # y-Koordinate
    y_geburtsdatum = 180
    y_adresse = 205  # y-Koordinate
    y_email = 252
    y_medizinische_verordnung = 275
    y_kv_nummer = 373
    y_datum = 800
    x_name = 110  # x-Koordinate
    x_text = 300  # x-Koordinate
    x_datum = 70

    seite.insert_text((x_name, y_name), text_name, fontsize=10, rotate=0, color=(0, 0, 0), overlay=True)
    seite.insert_text((x_text, y_geburtsdatum), text_geburtsdatum, fontsize=10, rotate=0, color=(0, 0, 0), overlay=True)
    seite.insert_text((x_text, y_adresse), text_adresse, fontsize=10, rotate=0, color=(0, 0, 0), overlay=True)
    seite.insert_text((x_text, y_email), text_email, fontsize=10, rotate=0, color=(0, 0, 0), overlay=True)
    seite.insert_text((x_text, y_medizinische_verordnung), text_medizinische_verordnung, fontsize=10, rotate=0,
                      color=(0, 0, 0), overlay=True)
    seite.insert_text((x_text, y_kv_nummer), text_kv_nummer, fontsize=10, rotate=0, color=(0, 0, 0), overlay=True)
    seite.insert_text((x_datum, y_datum), text_datum, fontsize=15, rotate=0, color=(0, 0, 0), overlay=True)


def gegenstand_der_verordnung_einlagen():
    x_kreuz_einlagen = 340

    seite.draw_line(fitz.Point(x_kreuz_einlagen, y_kreuz_verordnung),
                    fitz.Point(x_kreuz_einlagen + breite, y_kreuz_verordnung + hoehe))
    seite.draw_line(fitz.Point(x_kreuz_einlagen, y_kreuz_verordnung + hoehe),
                    fitz.Point(x_kreuz_einlagen + breite, y_kreuz_verordnung))


def gegenstand_der_verordnung_zurichtung():
    x_kreuz_zurichtung = 428

    seite.draw_line(fitz.Point(x_kreuz_zurichtung, y_kreuz_verordnung),
                    fitz.Point(x_kreuz_zurichtung + breite, y_kreuz_verordnung + hoehe))
    seite.draw_line(fitz.Point(x_kreuz_zurichtung, y_kreuz_verordnung + hoehe),
                    fitz.Point(x_kreuz_zurichtung + breite, y_kreuz_verordnung))


def gegenstand_der_verordnung_os():
    x_kreuz_os = 484

    seite.draw_line(fitz.Point(x_kreuz_os, y_kreuz_verordnung),
                    fitz.Point(x_kreuz_os + breite, y_kreuz_verordnung + hoehe))
    seite.draw_line(fitz.Point(x_kreuz_os, y_kreuz_verordnung + hoehe),
                    fitz.Point(x_kreuz_os + breite, y_kreuz_verordnung))


def sonstiges(text_sonstiges):
    x_sonstiges = 350
    y_sonstiges = 337
    seite.insert_text((x_sonstiges, y_sonstiges), text_sonstiges, fontsize=12, rotate=0, color=(0, 0, 0), overlay=True)


def werbung_ja():
    x_kreuz_werbung_ja = 398
    seite.draw_line(fitz.Point(x_kreuz_werbung_ja, y_kreuz_werbung),
                    fitz.Point(x_kreuz_werbung_ja + breite, y_kreuz_werbung + hoehe))
    seite.draw_line(fitz.Point(x_kreuz_werbung_ja, y_kreuz_werbung + hoehe),
                    fitz.Point(x_kreuz_werbung_ja + breite, y_kreuz_werbung))


def werbung_nein():
    x_kreuz_werbung_nein = 180
    seite.draw_line(fitz.Point(x_kreuz_werbung_nein, y_kreuz_werbung),
                    fitz.Point(x_kreuz_werbung_nein + breite, y_kreuz_werbung + hoehe))
    seite.draw_line(fitz.Point(x_kreuz_werbung_nein, y_kreuz_werbung + hoehe),
                    fitz.Point(x_kreuz_werbung_nein + breite, y_kreuz_werbung))


# PDF-Datei speichern
pdf.save('/register/pdfHandhabung/temporäre pdf/Datenschutz.pdf',  incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP)
pdf.close()