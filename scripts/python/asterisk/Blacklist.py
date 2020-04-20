#!/usr/bin/env python3.7
import sys
import paramiko
import urllib.parse
from pymongo import MongoClient


def getUnit(unit):
    username = urllib.parse.quote_plus('root')
    password = urllib.parse.quote_plus('Yjjnhjgbk_2019')
    connection = MongoClient(f"mongodb://{username}:{password}@192.168.99.190")
    db = connection['RBT']
    collection = db['UNITS']
    # Get one object of DB
    pile = collection.find_one({'Name': unit})
    if len(pile) == 0:
        return 'null'
    else:
        return pile


def execut(ip, cmd):
    key = paramiko.RSAKey.from_private_key_file("/home/glitch/.ssh/ats_rsa")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=ip, username='root', pkey=key)
    ssh.exec_command(cmd)
    ssh.close()


def addInBlacklist(unit, number):
    ip = getUnit(unit)['PBX']['IP']
    cmd = f'asterisk -rx "database put blacklist {number} 1"'
    execut(ip, cmd)


addInBlacklist(sys.argv[1], sys.argv[2])
