#!/usr/bin/python3.6
# -*- coding: utf-8
import sys
sys.path.append("/home/glitch/script/python/library/")
import mongo

def vATCinfo(name, domain, user, password, service = 'vATC'):
    data = {'Domain': domain,
            'Login': user,
            'Password': password}
    Stype = {'PBX.Service': service}
    Sdata = {f'PBX.{service}': data}
    mongo.update(name, Stype)
    mongo.update(name, Sdata)


def trunkInfo(name, host, user, authUser, password, service = 'Trunk'):
    data = {'Host': host,
            'User': user,
            'AuthUser': authUser,
            'Password': password}
    Stype = {'PBX.Service': service}
    Sdata = {f'PBX.{service}': data}
    mongo.update(name, Stype)
    mongo.update(name, Sdata)


def work(name, type):
    if type == 1:
        domain = input('Enter the domain of service: ')
        user = input('Enter the user of service user: ')
        password = input('Enter the password for the service: ')
        vATCinfo(name, domain, user, password)
    elif type == 2:
        host = input('Enter the domain of service: ')
        user = input('Enter the user of service user: ')
        authUser = input('Enter the authorized user of service user: ')
        password = input('Enter the password for the service: ')
        trunkInfo(name, host, user, authUser, password)
    else:
        print('Again!')
        work(name, type)


name = input('Enter the subdivision name: ')
type = int(input('Select type:\nvATC -> 1\nSIP trunk -> 2\nYour choice: '))

work(name, type)
