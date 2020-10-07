# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 23:34:49 2020


"""

#!/usr/bin/env python3
import os
import datetime
import reports
import emails
BASEPATH_SUPPLIER_TEXT_DES = os.path.expanduser('~') + '/supplier-data/descriptions/'
list_text_files = os.listdir(BASEPATH_SUPPLIER_TEXT_DES)


current_date = datetime.datetime.now().strftime('%Y-%m-%d')

report = []

def process_data(data):
	for item in data:
		report.append("name: {}<br/>weight: {}\n".format(item[0], item[1]))
	return report

text_data = []
for text_file in list_text_files:
	with open(BASEPATH_SUPPLIER_TEXT_DES + text_file, 'r') as f:
		text_data.append([line.strip() for line in f.readlines()])
		f.close()

if __name__ == "__main__":
    attachment = "/tmp/processed.pdf"
    title = "Processed Update on" + current_date
    summary = process_data(text_data)
    paragraph = "<br/><br/>".join(summary)
    reports.generate_report(attachment, title, paragraph)
    
    #generate email information
    sender = "automation@example.com"
    recipient = "username@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    
    #generate email with the report and attachment
    message = emails.generate_email(sender, recipient, subject, body, attachment=attachment)
    emails.send_email(message)