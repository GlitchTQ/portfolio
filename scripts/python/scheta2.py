#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# ver 4.0

import pymysql
import datetime
import csv
import os


def payment(unit):
    conect = pymysql.connect(host="192.168.XXX.XXX",
                             user="paha",
                             password="kozilok",
                             db="Billing",
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
    sql = (f"SELECT Salon_location.salon, YYYYY_{unit}.payment, "
           f"YYYYY_{unit}.location, Salon_location.unit "
           f"FROM Salon_location, YYYYY_{unit} "
           f"WHERE YYYYY_{unit}.location = Salon_location.location "
           f"AND Salon_location.unit = '{unit}'")
    cursor = conect.cursor()
    cursor.execute(sql)
    result = []
    for row in cursor:
        result.append(row)
    return result


def fillSalonName(salon_list):
    salon_name = []
    for row in salon_list:
        if row['salon'] not in salon_name:
            salon_name.append(row['salon'])
    return salon_name


# Цикл заполняющий переменные и список shet_list
def fillShetList(salon_name, salon_list):
    inet_line = 'Интернет'
    inet_sum = 0
    fiber = 'канала'
    phone_sum = 0
    itog_sum = 0
    itog_inet = 0
    itog_line = 0
    shet_list = {'Name': {'Inet': 'Inet', 'Phone': 'Phone'}}
    for name in salon_name:
        for salon in salon_list:
            if name == salon['salon']:
                if inet_line in salon['location'] or \
                   fiber in salon['location']:
                    inet_sum += salon['payment']
                else:
                    phone_sum += salon['payment']

        if name == 'salon06':
            inet_sum = inet_sum - 10000
        elif name == 'poligon':
            inet_sum = inet_sum + 10000

        itog_sum += inet_sum
        itog_sum += phone_sum
        itog_inet += inet_sum
        itog_line += phone_sum
        service = {'Inet': round(inet_sum, 2), 'Phone': round(phone_sum, 2)}
        shet_list.update({name: service})
        phone_sum = 0
        inet_sum = 0

    shet_list.update({'Sum': {'Inet': round(itog_inet, 2),
                              'Phone': round(itog_line, 2)}})
    return shet_list


def writeFiles(unit):
    shet_file = f'{os.getcwd()}\\shet_{unit}-{datetime.date.today()}.csv'
    salon_list = payment(unit)
    salon_name = fillSalonName(salon_list)
    shet_list = fillShetList(salon_name, salon_list)
    with open(shet_file, 'w', newline='') as f:
        fieldnames = ['Name', 'Inet', 'Phone']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        for key, value in shet_list.items():
            writer.writerow({'Name': key, 'Inet': value['Inet'],
                             'Phone': value['Phone']})


units = ['brend', 'fil', 'gol', 'korv', 'krv', 'os', 'XXX']

for unit in units:
    writeFiles(unit)
