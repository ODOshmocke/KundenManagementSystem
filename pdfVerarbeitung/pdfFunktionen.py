import os

PDF_KUNDEN_VERZEICHNISS = "KundenManagementSystem/pdfVerarbeitung/pdfKundenVerzeichniss"


def verzeichnissNamenErstellen(kunde):
    return str(kunde.id + "_" + kunde.vorname + "_" + kunde.nachname).lower()


def verzeichnissErstellen(kunde):
    verzeichnissName = verzeichnissNamenErstellen(kunde)
    if not os.path.exists(verzeichnissName):
        os.makedirs(verzeichnissName)
    return verzeichnissName