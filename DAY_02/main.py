from email.message import EmailMessage
import smtplib, ssl

Sender = 'your_name@email.com'         # Replace with ur gmail
Password = 'your_password'			   # Replace with ur password

Receiver = 'receiver_name@email.com'   # Replace with receiver email

sub = 'Welcome to Kurious School !'
body = '''
        Follow for more intresting contents - iKurious 
'''

em = EmailMessage()  
em['From'] = Sender
em['To'] = Receiver
em['Subject'] = sub
em.set_content(body)

context = ssl.create_default_context()  # Use SSL for security

with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smpt:
    smpt.login(Sender, Password)      # 465 - an SMPT port number 
    smpt.sendmail(Sender, Receiver, em.as_string())