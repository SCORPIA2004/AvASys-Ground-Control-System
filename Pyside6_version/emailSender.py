import smtplib
import csv
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication




def sendEmail(receipientEmail):
    # Fill in the details for your email account
    sender_email = "mshayanalwaha@gmail.com"
    app_password = "uluaskwkgccmjgxr"

    # List of email addresses
    # recipients = receipientEmail

    # Connect to the email server using SSL
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(sender_email, app_password)

    # Compose the message as a MIME message
    message = MIMEMultipart()

    # Add the body of the email to the MIME message
    message.attach(MIMEText("Neo Stellar"))

    # Set the headers for the email
    message["Subject"] = "Yo, thanks for signing up"
    message["From"] = sender_email
    message["To"] = receipientEmail

    # Send the email
    server.sendmail(sender_email, receipientEmail, message.as_string())
    print(f"Sent email to {receipientEmail}")

    # Close the connection to the email server
    server.quit()