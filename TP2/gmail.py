# coding: utf8

import json
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


def get_config_email():
    with open('config.json', 'r') as f:
        config = json.load(f)
    return config


def envoyer_email(destination_address):
    config = get_config_email()

    source_address = config['email']
    body = "Testetetststststst2121"
    subject = "I send mails!"

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