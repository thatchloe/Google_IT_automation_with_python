# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 23:58:59 2020

"""


#!/usr/bin/env python3
import email.message 
import mimetypes
import os.path
import smtplib

def generate_email(sender, recipient, subject, body, attachment = None):
    message = email.message.EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)
    
    if attachment != None:
        attachment_name = os.path.basename(attachment)
        mime_type, _ = mimetypes.guess_type(attachment)
        mime_type, subtype = mime_type.split("/", 1)
        with open(attachment, 'rb') as file:
            message.add_attachment(file.read(),
                                   maintype = mime_type,
                                   subtype = subtype,
                                   filename = attachment_name)
    return message

def send_email(message):
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()



def generate_error_report(sender, recipient, subject, body):

  message = email.message.EmailMessage()
  message["From"] = sender
  message["To"] = recipient
  message["Subject"] = subject
  message.set_content(body)

  return message