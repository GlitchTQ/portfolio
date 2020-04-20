#!/usr/bin/python3.7
# -*- coding: utf-8
# Send mail.
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

# Функция отправки почты


def XXXAttachment(target, themes, message):
    msg = MIMEMultipart()
    # setup the parameters of the message
    password = "password"
    msg['From'] = "noreply@god2.XXX.ru"
    msg['To'] = target
    msg['Subject'] = themes
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    # Here need a 'for' for attachments
    filename = "1"
    filename1 = "2"
    attachment = open("/home/glitch/Pictures/wallpapers/abandoned-forest-industry-nature-34950.jpg", "rb")
    attachment1 = open("/home/glitch/Pictures/wallpapers/asphalt-dark-dawn-endless-531321.jpg", "rb")
    p = MIMEBase('application', 'octet-stream')
    z = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    z.set_payload((attachment1).read())
    encoders.encode_base64(p)
    encoders.encode_base64(z)
    p.add_header('Content-Disposition', f"attachment; filename={filename}")
    z.add_header('Content-Disposition', f"attachment; filename={filename1}")
    msg.attach(p)
    msg.attach(z)

    smtp_server = 'god2.XXX.ru'
    smtp_port = 587
    XXXmail = smtplib.SMTP(smtp_server, smtp_port)
    XXXmail.starttls()
    XXXmail.login(msg['From'], password)
    XXXmail.sendmail(msg['From'], msg['To'], msg.as_string())
    XXXmail.quit()


XXXAttachment('555@XXX.ru', '1', '1')
