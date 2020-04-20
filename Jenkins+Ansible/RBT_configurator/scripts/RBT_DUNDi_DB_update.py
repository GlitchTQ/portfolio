#!/usr/bin/env python3.7
import sys
import pymysql
import urllib.parse
from pymongo import MongoClient


def getOne(name):
    def connect():
        # Connection to DB
        username = urllib.parse.quote_plus('root')
        password = urllib.parse.quote_plus('Pasword')
        connection = MongoClient(f"mongodb://{username}:{password}"
                                 f"@192.168.XXX.XXX")
        db = connection['XXX']
        collection = db['UNITS']
        return collection
    # Get one object of DB
    pile = connect().find_one({'Name': name})
    if len(pile) == 0:
        return 'null'
    else:
        return pile


def SQLconnect():
    conect = pymysql.connect(host="192.168.XXX.XXX",
                             user="onec",
                             password="Pasword",
                             db="cdrdb",
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    return conect


def pushMask(name, mask):
    INFO = getOne(name)
    sql = (f'INSERT INTO asterisk.dundi '
           f'(`S_name`, `Mask`, `IP`)'
           f'VALUES '
           f'("{INFO["Name"]}", "{mask}", "{INFO["PBX"]["IP"]}");')
    cursor = SQLconnect().cursor()
    cursor.execute(sql)


pushMask(sys.argv[1], sys.argv[2])
