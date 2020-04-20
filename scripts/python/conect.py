#!/usr/bin/env python3.7
# -*- coding: utf-8
import os
import sys
import colorama
from library import mongo
from library import reach


colorama.init()
RED = colorama.Fore.RED
GRN = colorama.Fore.GREEN
BLE = colorama.Fore.BLUE
MGA = colorama.Fore.MAGENTA
END = colorama.Style.RESET_ALL

PBXkey = 'path to key'
DevilKey = 'path to key'
EdgeKey = 'path to key'


def connectPBX(unit):
    ip = mongo.getOne(unit)['PBX']['IP']
    print(f'{MGA}Connect to PBX {unit}.\n{GRN}IP: {ip}{END}')
    os.system(f'ssh root@{ip} -i {PBXkey}')


def connectServer(unit):
    DATA = mongo.connect().find_one({'Name': unit, 'Unit': 'Server'})
    IP = DATA['IN_IP']
    RPORT = DATA['Rport']
    print(f'{MGA}Connect to Server {unit}.\n{GRN}IP: {IP}{END}')
    os.system(f'ssh root@{IP} -p {RPORT} -i {PBXkey}')


def connectRouter(unit):
    DATA = mongo.getOne(unit)
    IN_IP = DATA['Router']['IN_IP']
    RTYPE = DATA['Router']['Rtype']
    RPORT = DATA['Router']['Rport']
    print(f'{MGA}Connect to Router {unit}.{END}')
    if RTYPE == 'Devil':
        os.system(f'ssh root@{IN_IP} -p {RPORT} -i {DevilKey}')
    elif RTYPE == 'Edge':
        os.system(f'ssh ubnt@{IN_IP} -p {RPORT} -i {EdgeKey}')
    else:
        print('You sure?')


def reachUnit(unit):
    DATA = mongo.getOne(unit)
    if DATA is None:
        print(f'Unit {unit} is not exist!')
    else:
        ips = {'Router in': DATA['Router']['IN_IP'],
               'Router out': DATA['Router']['OUT_IP'],
               'PBX': DATA['PBX']['IP']}
        for key, ip in ips.items():
            if ip[0] == '1':
                status = reach.ping(ip)
                if status == 'offline':
                    print(f'{MGA}{key}: {GRN}is {RED}{status}.{END}')
                else:
                    print(f'{MGA}{key}: {GRN}is {status}.{END}')
            else:
                print(f'{MGA}{key}: {RED}is not set.{END}')


def connect(what, unit):
    if what == 'p':
        connectPBX(unit)
    elif what == 'g':
        connectRouter(unit)
    elif what == 's':
        connectServer(unit)
    elif what == 'r':
        reachUnit(unit)
    else:
        print(f'1. What? ((g)ate way, (p)bx or (s)erver)\n'
              f'2. Unit? (S#, L#, H# or Server name)')


try:
    connect(sys.argv[1], sys.argv[2])
except TypeError:
    print(f'{RED}Update the Database.{END}')
except IndexError:
    print(f'{RED}Indicate what you need.{END}')
