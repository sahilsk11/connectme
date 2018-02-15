#!/usr/bin/python
import smtplib
import passwords

class notification:


    def __init__(self, target_email):
        self.receiver = target_email
        
    def send_email(self):
        SMTP_SERVER = 'smtp.gmail.com'
        SMTP_PORT = 587
        GMAIL_USERNAME = 'iotspace.tech@gmail.com'
        GMAIL_PASSWORD = passwords.email() #CAUTION: This is stored in plain text!
        
        print(GMAIL_PASSWORD)
        recipient = self.receiver
        subject = 'Someone has applied for your event!'
        emailText = 'Hello, a user has applied for your event.'
        
        emailText = "" + emailText + ""
        
        headers = ["From: " + GMAIL_USERNAME,
                   "Subject: " + subject,
                   "To: " + recipient,
                   "MIME-Version: 1.0",
                   "Content-Type: text/html"]
        headers = "\r\n".join(headers)
        
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        
        session.ehlo()
        session.starttls()
        session.ehlo
        
        session.login(GMAIL_USERNAME, GMAIL_PASSWORD)
        
        session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + emailText)
        session.quit()