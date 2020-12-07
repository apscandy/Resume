import smtplib
import pandas as pd
from email.message import EmailMessage
EmailAddressSender = "xxx@xxx.com"
EmailPassword = "********"
EmailAddressList = pd.read_excel("Emails.xlsx")
EmailAddressReceiver = EmailAddressList["Emails"].values
with open("EmailBodyText.txt", "r") as BlockText:
    BlockText_body = BlockText.read()
msg = EmailMessage()
msg['Subject'] = 'expression of interest'
msg['From'] = EmailAddressSender
msg['Cc'] = "xxx@xxx.com"
msg['Bcc'] = EmailAddressReceiver
msg.set_content(BlockText_body)
files = ['Profile.pdf']
for file in files:
    with open(file, 'rb') as PDF:
        file_data = PDF.read()
        file_name = PDF.name
    msg.add_attachment(file_data, maintype = "application", subtype = 'octet-stream', filename = file_name)
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(EmailAddressSender, EmailPassword)
    smtp.send_message(msg)
