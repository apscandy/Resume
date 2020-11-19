# --- Imports ---

import smtplib
import imghdr
from email.message import EmailMessage

# --- Email login details ---

EmailAddressSender = "andrews.python.app@gmail.com"
EmailPassword = "Wolf3636"

# --- who I'm send the emails to ---

EmailAddressReceiver = ["andrewclarke.aron@gmail.com", "tashb459@gmail.com"]

# --- Email Message ---

msg = EmailMessage()
msg['Subject'] = 'Resume test SSL'
msg['From'] = EmailAddressSender
msg['Bcc'] = EmailAddressReceiver
msg.set_content("testing the SSL")

# --- Adding an Image ---
'''
with open('logo.jpg', 'rb') as Image:
    file_data = Image.read()
    file_type = imghdr.what(Image.name)
    file_name = Image.name
msg.add_attachment(file_data, maintype = "image", subtype = file_type, filename = file_name)
'''
# --- Sending mulitple images ---
'''
files = ['logo.jpg', 'cool.png']
for file in files:
    with open(file, 'rb') as Image:
        file_data = Image.read()
        file_type = imghdr.what(Image.name)
        file_name = Image.name
    msg.add_attachment(file_data, maintype = "image", subtype = file_type, filename = file_name)
'''
# --- Sending PDFs ---

files = ['Profile.pdf']
for file in files:
    with open(file, 'rb') as PDF:
        file_data = PDF.read()
        file_name = PDF.name
    msg.add_attachment(file_data, maintype = "application", subtype = 'octet-stream', filename = file_name)

# --- SMTP over TLS ---

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(EmailAddressSender, EmailPassword)
    smtp.send_message(msg)

# --- SMTP over SSL ---
'''
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EmailAddressSender, EmailPassword)
'''
