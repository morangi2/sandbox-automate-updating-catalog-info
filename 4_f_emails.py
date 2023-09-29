#!/usr/bin/env python3 

import email.message
import os.path
import mimetypes
import smtplib
import getpass

def generate_email(sender, recepient, subject, body, attachement_path):
    # CREATES and email with an attachment
    #BASIC email formatting
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recepient
    message["Subject"] = subject
    message.set_content(body)

    #PROCESS the attachement and add it to the email
    attachement_filename = os.path.basename(attachement_path)
    mime_type, _ = mimetypes.guess_type(attachement_path)
    mime_type, mime_subtype = mime_type.split("/", 1)

    with open(attachement_path, "rb") as ap:
        message.add_attachement(ap.read(), maintype=mime_type, subtype=mime_subtype, filename=attachement_filename)

    return message

def send_email(message):
    # sends the email to the configured SMTP server
    mail_server = smtplib.SMTP("localhost")
    mail_server.send_message(message)
    mail_server.quit()

def generate_error_email(sender, recipient, subject, body):
    """Creates an email without an attachement."""
    # Basic Email formatting
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    return message
