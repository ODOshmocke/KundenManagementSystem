import os

PDF_KUNDEN_VERZEICHNISS = "KundenManagementSystem/pdfVerarbeitung/kundenunterlagen/"


def verzeichnissNamenErstellen(kunde):
    return str(str(kunde.id) + "_" + kunde.vorname + "_" + kunde.nachname).lower()


def verzeichnissErstellen(kunde, weg):
    verzeichnissName = verzeichnissNamenErstellen(kunde)
    kommpletteWegZumKundenverzeichnis = os.path.join(weg, verzeichnissName)
    verzeichnissExistiert = os.path.exists(kommpletteWegZumKundenverzeichnis)
    if not verzeichnissExistiert:
        os.makedirs(kommpletteWegZumKundenverzeichnis)
    return verzeichnissName, kommpletteWegZumKundenverzeichnis, verzeichnissExistiert
