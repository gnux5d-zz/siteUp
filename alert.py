import sys
import os
import smtplib, ssl

import requests

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def SendingMail(messageFile, contactsFile):
    # creating server and connecting
    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context)
        server.login(sender_email, password)

        # fetching the body of message
        with open(messageFile, 'r', encoding='utf-8') as body:
            message = body.read()

        msg = MIMEMultipart() # create a 'message' object

        for line in open(contactsFile).readlines():
            contact = line.strip("\n")

            msg['From'] = sender_email
            msg['To']= contact
            msg['Subject'] = "Alert!"

            msg.attach(MIMEText(message, 'plain'))

            server.send_message(msg)

    except Exception as e:
        print(e)

    finally:
        server.quit()

def CheckingURL(url):
    r = requests.get(url)

    return r.status_code

workingDirectory = os.getcwd()

messageFile = workingDirectory + "/message.txt"
sourceFile = workingDirectory + "/source.txt"
contactsFile = workingDirectory + "/contacts.txt"

# Checking if all files exist
if not os.path.isfile(messageFile):
    print("Missing message.txt file. If it exist, check for typo.")
    sys.exit()
if not os.path.isfile(sourceFile):
    print("Missing source.txt file. If it exist, check for typo.")
    sys.exit()
if not os.path.isfile(contactsFile):
    print("Missing contacts.txt file. If it exist, check for typo.")
    sys.exit()


# Setting up the server and port to connection
port = 587
smtp_server = "smtp.gmail.com"

source = open(sourceFile).readlines()
# Checking the structure of source file and printout the correct format in any error case.
if len(source) > 2:
    print("Usage ERROR: source file must contain sender email and password, e.g.:")
    print("email: xxxxx@xx.com")
    print("password: thepassword")
    sys.exit()

# picking up the sender e-mail and password.
else:
    sender_email = source[0].split(":")[1].strip(" ").strip("\n")
    password = source[1].split(":")[1].strip(" ").strip("\n")

# The url to check for some metadata and return whatever you want.
url = "http://www.google.com"
metadata = CheckingURL(url)

# checking the expected metadata and sending the email based on its value.
if metadata != 200:
    SendingMail(messageFile, contactsFile)
    print("Crash!")
else:
    print("Ok!")
