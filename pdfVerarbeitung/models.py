from django.db import models
from django import forms


# Create your models here.

class PdfInformationDatenschutz(forms.Form):
    # Datenschutz.py
    medizinische_verordnung_model = forms.CharField(max_length=100, required=False, label="Medizinische Verordnung")
    gegenstand_der_verordnung_einlagen_model = forms.BooleanField(required=False, label="Gegenstand der Verordnung: "
                                                                                        "Einlagen")
    gegenstand_der_verordnung_zurichtung_model = forms.BooleanField(required=False, label="Gegenstand der Verordnung: "
                                                                                          "Zurichtung")
    gegenstand_der_verordnung_os_model = forms.BooleanField(required=False, label="Gegenstand der Verordnung: OS")
    sonstiges_model = forms.CharField(max_length=200, required=False, label="Gegenstand der Verordnung: Sonstiges")
    werbung_ja_model = forms.BooleanField(required=False, label="Werbung: Ja")
    werbung_nein_model = forms.BooleanField(required=False, label="Werbung: Nein")

class PdfInformationPatientenerklärung(forms.Form):
    # Patientenerklörung.py
    ich_noch_keine_orthopaedischen_schuhzurichtungenerhalten_habe_erstmalige_versorgung_model = forms.BooleanField(
        required=False, label="Ich noch keine orthopädischen Schuhzurichtungen erhalten habe (erstmalige Versorgung)")
    ich__im__rahmen__der__erstmaligen__versorgung__erst__1__paar__orthopaedische__schuhzurichtungen_erhalten_habe_model = forms.BooleanField(
        required=False, label="Ich im Rahmen der erstmaligen Versorgung erst 1 Paar orthopädische Schuhzurichtungen erhalten habe")
    ich_im_rahmen_der_erstmaligen_versorgung_erst_2_paar_orthopaedische_schuhzurichtungen_erhalten_habe_model = forms.BooleanField(
        required=False, label="Ich im Rahmen der erstmaligen Versorgung erst 2 Paar orthopädische Schuhzurichtungen erhalten habe")
    ich__in__den__vergangenen__6__monaten__noch__keine__weitere__orthopaedische__schuhzurichtung_erhalten_habe_model = forms.BooleanField(
        required=False, label="Ich in den vergangenen 6 Monaten noch keine weitere orthopädische Schuhzurichtung erhalten habe")
    ich_noch_keine_einlagen_erhalten_habeerstmalige_versorgung_model = forms.BooleanField(required=False, label="Ich noch keine Einlagen erhalten habe (erstmalige Versorgung)")
    ich__im__rahmen__der__erstmaligen__versorgung__erst__1__paar__einlagen__erhalten__habe__welche_ausreichend_mit_positivem_ergebnis_erprobt_wurden_wechselpaar_model = forms.BooleanField(
        required=False, label="Ich im Rahmen der erstmaligen Versorgung erst 1 Paar Einlagen erhalten habe, welche ausreichend mit positivem Ergebnis erprobt wurden (Wechselpaar)")
    ich_innerhalb_der_letzten_12_monate_model = forms.BooleanField(required=False, label="Ich innerhalb der letzten 12 Monate")
    keine_einlagen_oder_model = forms.BooleanField(required=False, label="keine Einlagen oder")
    erst_ein_paar_einlagenerhalten_habe_model = forms.BooleanField(required=False, label="erst 1 Paar Einlagen erhalten habe")
    dass_ich_nicht_mit_orthopaedischen_schuhenversorgt_wurde_model = forms.BooleanField(required=False)
    datum_stempel_text_model = forms.CharField(max_length=200, required=False)

class PdfInformationHöherwerigeversorgung(forms.Form):
    # höherwerigeversorgung.py
    ich_habe_mich_fuer_eine_versorgung_mit_aufzahlung_mehrkosten_entschieden_model = forms.BooleanField(required=False, label="Ich habe mich für eine Versorgung mit Aufzahlung/Mehrkosten entschieden")
    ich_habe_mich_fuer_folgende_versorgung_entschieden_model = forms.CharField(max_length=200, required=False, label="Ich habe mich für folgende Versorgung entschieden")

