import smtplib
import pandas as pd
from email.message import EmailMessage

# --- Email login details ---

EmailAddressSender = "andrews.python.app@gmail.com"
EmailPassword = "Wolf3636"

# --- who I'm sending the emails to ---

EmailAddressList = pd.read_excel("Emails.xlsx")
EmailAddressReceiver = EmailAddressList["Emails"].values

# --- Content ---

with open("EmailBodyText.txt", "r") as BlockText:
    BlockText_body = BlockText.read()

# --- Email Message ---

msg = EmailMessage()
msg['Subject'] = 'expression of interest'
msg['From'] = EmailAddressSender
msg['Cc'] = "andrewclarke.aron@gmail.com"
msg['Bcc'] = EmailAddressReceiver
msg.set_content(BlockText_body)

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

# --- End of program ---
