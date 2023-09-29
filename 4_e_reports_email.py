#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
from reportlab.lib.units import inch
import os
from datetime import date
import 4_f_reports
import sys

def process_data():
    #load feedback entries into dctionary
    summary = ""
    for file in files:
        # A -- read all the lines (there's 3 lines in each, we only need name[1] and weight [2])
        lines = readeachfile(file)
        print(lines) #prints all the lines

        name = lines[0]
        weight = lines[1]
        per_fruit_summary = "Name: " + name + "<\n>" + "Weight: " + weight + "<\n>" + "<\n>"

        summary = summary + per_fruit_summary

    return summary

if __name__ == "__main__":
    summary = process_data()
    reports.generate_report("/tmp/processed.pdf", date, summary)
    sender = "automation@example.com"
    receiver = "<USERNAME>@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

    #send pdf report as an email attachment

    message = 4_f_emails.generate_email(sender, receiver, subject, body, "/tmp/processed.pdf")
    4_f_emails.send_email(message)
