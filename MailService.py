# MailService.py
#
# Handles the connection to mail server and receivers
#
# @author   Orhun Dalabasmaz
# @since    Dec, 2016

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config.MailConfig import *

SMTP_SSL_PORT = 465


def connect_to_mail_server():
    if server_port == SMTP_SSL_PORT:
        mail_server = smtplib.SMTP_SSL(server_address, server_port)
    else:
        mail_server = smtplib.SMTP(server_address, server_port)
    mail_server.set_debuglevel(mail_server_debug_enabled)
    mail_server.starttls()
    mail_server.login(sender_address, sender_password)
    return mail_server


def send_mail(mail_subject, mail_content):
    mail_server = connect_to_mail_server()

    # Create the message
    msg = MIMEMultipart()
    msg['From'] = sender_address
    msg['To'] = ", ".join(receiver_addresses)
    msg['CC'] = ", ".join(receiver_addresses_cc)
    msg['BCC'] = ", ".join(receiver_addresses_bcc)
    msg['Subject'] = mail_subject
    msg.attach(MIMEText(mail_content, 'html'))

    try:
        mail_server.sendmail(sender_address, receiver_addresses, msg.as_string())
    except EOFError:
        print "Error occurred when sending mail."
    mail_server.quit()
