from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib, ssl

Sender = 'sender@email.com'         # Replace with ur gmail
Password = '********'			   # Replace with ur password

Receiver = 'receiver@email.com'   # Replace with receiver email

sub = 'Welcome to Kurious School - Attachment!'
body = '''
        Follow for more intresting contents - iKurious 
'''

em = MIMEMultipart()  
em['From'] = Sender
em['To'] = Receiver
em['Subject'] = sub
em.attach(MIMEText(body, 'plain'))

attachment = 'logo.png'
attach_file = open(attachment, 'rb') 
payload = MIMEBase('application', 'octate-stream')
payload.set_payload((attach_file).read())
encoders.encode_base64(payload)   # Binary -> Encode -> add header
payload.add_header('Content-Decomposition', 'attachment', filename=attachment)
em.attach(payload)


context = ssl.create_default_context()  # Use SSL for security

with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smpt:
    smpt.login(Sender, Password)      # 465 - an SMPT port number 
    smpt.sendmail(Sender, Receiver, em.as_string())
    smpt.quit()
    print('Mail sent ! ! !')