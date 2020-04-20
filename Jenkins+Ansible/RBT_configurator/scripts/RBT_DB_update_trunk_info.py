#!/usr/bin/env python3.6
# -*- coding: utf-8
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


def vATCinfo(name, host, user, password, service='vATC'):
    data = {'Domain': host,
            'Login': user,
            'Password': password}
    Stype = {'PBX.Service': service}
    Sdata = {f'PBX.{service}': data}
    update(name, Stype)
    update(name, Sdata)


def trunkInfo(name, host, user, authUser, password, service='Trunk'):
    data = {'Host': host,
            'User': user,
            'AuthUser': authUser,
            'Password': password}
    Stype = {'PBX.Service': service}
    Sdata = {f'PBX.{service}': data}
    update(name, Stype)
    update(name, Sdata)


def execution(name, host, user, authUser, password, service):
    if service == 'vATC':
        vATCinfo(name, host, user, password, service)
    elif service == 'Trunk':
        trunkInfo(name, host, user, authUser, password, service)


execution(sys.argv[1], sys.argv[2], sys.argv[3],
          sys.argv[4], sys.argv[5], sys.argv[6])
