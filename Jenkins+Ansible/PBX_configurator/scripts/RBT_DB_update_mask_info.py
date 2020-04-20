#!/usr/bin/env python3.6
# -*- coding: utf-8
'''
Update DB
'''
import sys
import urllib.parse
from pymongo import MongoClient


def connect():
    # Connection to DB
    username = urllib.parse.quote_plus('root')
    password = urllib.parse.quote_plus('Pasword')
    connection = MongoClient(f"mongodb://{username}:{password}@192.168.XXX.XXX")
    db = connection['XXX']
    collection = db['UNITS']
    return collection


def update(name, data):
    # Update one unit in DB
    connect().update_one({'Name': name}, {'$set': data})


def maskUpDate(name, mask):
    data = {f'PBX.MASK': f'{mask}X'}
    update(name, data)


maskUpDate(sys.argv[1], sys.argv[2])
