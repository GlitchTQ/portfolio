#!/usr/bin/python3.6
# -*- coding: utf-8
import urllib.parse
from pymongo import MongoClient


def connect():
    # Connection to DB
    username = urllib.parse.quote_plus('root')
    password = urllib.parse.quote_plus('password')
    connection = MongoClient(f"mongodb://{username}:{password}@192.168.XXX.XXX")
    db = connection['XXX']
    collection = db['UNITS']
    return collection


def getOne(name):
    # Get one object of DB
    pile = connect().find_one({'Name': name})
    if pile is None:
        return 'null'
    else:
        return pile


def getPBX(ip):
    pile = connect().find_one({'PBX.IP': ip})
    if pile is None:
        pile = connect().find_one({'IN_IP': ip})
        if pile is None:
            return None
        else:
            return pile
    else:
        return pile


def getAll():
    # Get one object of DB
    pile = connect().find({})
    return pile


def getAllSalon():
    pile = connect().find({'Unit': 'Unit'})
    return pile


def update(name, data):
    # Update one unit in DB
    connect().update_one({'Name': name}, {'$set': data})
