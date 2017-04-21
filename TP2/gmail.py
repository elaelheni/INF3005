# coding: utf8
#
# author: Jean-Michel Poirier
# code: POIJ26089200

import json
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

RESET_PASSWORD_BODY_1 = "Bonjour\n" + \
                        "\n"+ \
                        "Pour changer votre mot de passe cliquer sur le lien ci-dessous:\n"
RESET_PASSWORD_BODY_2 = "\n" + \
                        "Si vous n'avez pas lance cette demande de recuperation de compte, ignorez ce courrier electronique. Nous garderons votre compte en securite."
RESET_PASSWORD_SUBJECT = u"Récupération du compte!"
ADD_ADMIN_BODY_1 = "Bonjour\n" + \
                   "\n"+ \
                   "Pour activer votre compte cliquer sur le lien ci-dessous:\n"
ADD_ADMIN_SUBJECT = "Activation de votre compte"


def get_config_email():
    with open('config.json', 'r') as f:
        config = json.load(f)
    return config


def email_contenu(url, template):
    dic = None
    if template == 1:
        body = RESET_PASSWORD_BODY_1 + url + "\n" + RESET_PASSWORD_BODY_2
        subject = RESET_PASSWORD_SUBJECT
        dic = {'Subject': subject, 'Body': body}
    elif template == 2:
        body = ADD_ADMIN_BODY_1 + url + "\n"
        subject = ADD_ADMIN_SUBJECT
        dic = {'Subject': subject, 'Body': body}
    return dic


def envoyer_email(destination_address, url, template):
    config = get_config_email()
    source_address = config['email']
    email_content = email_contenu(url, template)
    body = email_content['Body']
    subject = email_content['Subject']

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = source_address
    msg['To'] = destination_address
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(source_address, config['password'])
    text = msg.as_string()
    server.sendmail(source_address, destination_address, text)
    server.quit()

body2 = None

