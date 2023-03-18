import ssl
from email.message import EmailMessage
import smtplib

emailSender = "oskar.samsung.j5@gmail.com"
emailPassword = "vccevakprtyyvria"
emailReceiver = "oskarkammlodt@gmail.com"



subject = "Check this email address"


def send_mails(user):


    with open("C:/Users/oskar/IdeaProjects/form/EmailText.txt", "r") as r:
        body = r.read()

    # Benutzerspezifische Email
    body = body.replace("{Nachname}", user.nachname)
    body = body.replace("{Vorname}", user.vorname)
    body = body.replace("{Email}", user.email)
    body = body.replace("{Krankenkasse}", user.krankenkasse)

    if user.geschlecht == "Mann":
        body = body.replace("{Ansprache}", "Herr")

    elif user.geschlecht == "Frau":
        body = body.replace("{Ansprache}", "Frau")

'''

    print(body)

    em = EmailMessage()
    em["from"] = emailSender
    em["to"] = user.email
    print(user.email)
    em["subject"] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(emailSender, emailPassword)
        smtp.sendmail(emailSender, user.email, em.as_string())

'''