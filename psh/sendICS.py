# -*- coding: utf-8 -*-
# Import smtplib for the actual sending function
import smtplib

# Here are the email package modules we'll need
from email.mime.image import MIMEImage
from email.MIMEBase import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email import Encoders
import logging, argparse
import logging.handlers, logging.config

parser = argparse.ArgumentParser(description='CSV to VCF')
parser.add_argument('--data')
parser.add_argument('--output')
parser.add_argument('--user')
args = parser.parse_args()

dataProcess=args.data
userMail=args.user
outputDirectory=args.output

COMMASPACE = ', '
me = 'migration.exchange@iledefrance-mobilites.fr'
#family = ['prenom.nom@stif.info']
userSTIF = userMail + '@iledefrance-mobilites.fr'
#userSTIF = userMail + '@stif.info'
family = [userSTIF]

# Create the container (outer) email message.
msg = MIMEMultipart('alternative')
msg['Subject'] = Header('DSI/MIGRATION EXCHANGE - votre CALENDRIER à importer le 15 décembre au matin - ANNULE ET REMPLACE LE MAIL DE 20h30', 'utf-8')
# me == the sender's email address
# family = the list of all recipients' email addresses
msg['From'] = 'migration.exchange@iledefrance-mobilites.fr'
msg['To'] = COMMASPACE.join(family)
msg.preamble = 'Test d\'envoi ICS'

part = MIMEBase('application', "octet-stream")
part.set_payload(open(outputDirectory + userMail + "@iledefrance-mobilites.fr.ics", "rb").read())
Encoders.encode_base64(part)

part.add_header('Content-Disposition', 'attachment; filename="' + userMail + '@iledefrance-mobilites.fr.ics"')
msg.attach(part)

# Send the email via our own SMTP server.
#s = smtplib.SMTP('172.17.0.60')
s = smtplib.SMTP('172.17.3.7')
s.sendmail(me, family, msg.as_string())
s.quit()
