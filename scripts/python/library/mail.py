#!/usr/bin/python3.6
# -*- coding: utf-8
# Send mail.
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from os.path import basename
import smtplib


def XXXAttachment(target, themes, message, attachment):
    msg = MIMEMultipart()
    # setup the parameters of the message
    password = "password"
    msg['From'] = "noreply@god2.XXX.ru"
    msg['To'] = target
    msg['Subject'] = themes
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    with open(attachment, "rb") as attaches:
        part = MIMEApplication(attaches.read(),
                               Name=basename(attachment))
    part['Content-Disposition'] = (f'attachment; '
                                   f'filename="{basename(attachment)}"')
    msg.attach(part)
    smtp_server = 'god2.XXX.ru'
    smtp_port = 587
    XXXmail = smtplib.SMTP(smtp_server, smtp_port)
    XXXmail.starttls()
    XXXmail.login(msg['From'], password)
    XXXmail.sendmail(msg['From'], msg['To'], msg.as_string())
    XXXmail.quit()


def XXX(target, themes, message):
    msg = MIMEMultipart()
    # setup the parameters of the message
    password = "password"
    msg['From'] = "noreply@god2.XXX.ru"
    msg['To'] = target
    msg['Subject'] = themes
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    smtp_server = 'god2.XXX.ru'
    smtp_port = 587
    XXXmail = smtplib.SMTP(smtp_server, smtp_port)
    XXXmail.starttls()
    XXXmail.login(msg['From'], password)
    XXXmail.sendmail(msg['From'], msg['To'], msg.as_string())
    XXXmail.quit()
