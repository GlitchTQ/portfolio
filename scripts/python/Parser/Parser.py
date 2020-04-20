#!/usr/bin/env python3.7
import requests
from bs4 import BeautifulSoup as BFS
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

TARGETS = ('example@test.ru')
URL = 'https://www.kdez74.ru/HouseSearch/CutOffs'
HEADERS = {'User-Agent': (f'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          f'Chrome/80.0.3987.132 YaBrowser/20.3.2.282 (beta) Yowser/2.5 Safari/537.36'),
           'Accept': '*/*'}


def mail(target, themes, message):
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


def get_html(url):
    r = requests.get(url, headers=HEADERS)
    return r


def get_content(html):
    data = []
    soup = BFS(html, 'html.parser')
    table = soup.table
    table_body = table.find('tbody')
    table_rows = table_body.find_all('tr')

    for row in table_rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]

        for col in cols:
            if col:
                data.append(col)

    address = []
    tmp = []
    for adr in data:
        if str(adr)[0:3] == 'ул.':
            if adr:
                address.append(tmp)
            tmp = []
        else:
            tmp.append(adr)
    address.append(tmp)

    return address


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        addresses = get_content(html.text)
        for address in addresses:
            if address:
                if address[0] == 'address':
                    theme = f'ЖЭК. Событие: {address[1]}'
                    message = (f'{address[0]}\n'
                               f'{address[1]}\n'
                               f'Сроки {address[2]}\n'
                               f'Коментарий: {address[3]}\n'
                               f'Ссылка: {URL}')

                    for target in TARGETS:
                        mail(target, theme, message)
    else:
        print(f'Error: {html.status_code}')


parse()
