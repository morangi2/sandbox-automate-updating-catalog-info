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

file_src_dir = "supplier-data/descriptions"

#capture list of files
files = os.listdir(file_src_dir)


def generate_report(filename, title, pharagraph):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  report_info = Paragraph(pharagraph, styles["BodyText"])
  table_style = [("GRID", (0,0), (-1,-1), 1, colors.black), 
                  ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
                  ("ALIGN", (0,0), (-1,-1), "CENTER")]
  empty_line = Spacer(1,20)
  report.build([report_title, empty_line, report_info])

#read file lines into a list
def readeachfile(file):
    with open(file_src_dir + "/" + file) as f:
        lines = f.read().strip().splitlines() #REM split first, the splitlines
    return lines



