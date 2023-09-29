#!/usr/bin/env python3

import shutil
import psutil
import socket
import 4_f_emails
import os

sender = "automation@example.com"
receiver = "<USERNAME>@example.com"
body = "Please check your system and resolve the issue as soon as possible."


# Checks CPU usage and sends email if usage >80%
cpu_percentage = psutil.cpu_percent(1)
if cpu_percentage > 80:
    subject = "Error - CPU usage is over 80%"
    message = 4_f_emails.generate_error_email(sender, receiver, subject, body) 
    4_f_emails.send_email(message)

# Checks disk usage and sends email if available space < 20%
disk_u_space = shutil.disk_usage("/")
disk_u_sapce_percentage = disk_u_space.free / disk_u_space.total * 100
if disk_u_sapce_percentage < 20:
    subject = "Error - Available disk space is less than 20%"
    message = 4_f_emails.generate_error_email(sender, receiver, subject, body) 
    4_f_emails.send_email(message)

# Checks if available memory is less than 500MB
memory = psutil.virtual_memory()
trs = 500 * 1024 * 1024 # == 500MB
if memory.available < trs:
    subject = "Error - Available memory is less than 500MB"
    message = 4_f_emails.generate_error_email(sender, receiver, subject, body) 
    4_f_emails.send_email(message)

# Checks hostname and if cannot be resolved to "127.0.0.1" sends an email
hostname = socket.gethostbyname('localhost')
if hostname != '127.0.0.1':
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    message = 4_f_email.generate_error_email(sender, receiver, subject, body) 
    4_f_email.send_email(message)



