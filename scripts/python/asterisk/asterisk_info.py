#!/usr/bin/env python3.7
# -*- coding: utf-8

import colorama
# import re
import sys
from library import mongo
from library import ssh


colorama.init()
RED = colorama.Fore.RED
GRN = colorama.Fore.GREEN
BLE = colorama.Fore.BLUE
MGA = colorama.Fore.MAGENTA
END = colorama.Style.RESET_ALL

PBXkey = '/home/glitch/.ssh/ats_rsa'
DUNDiServer = '192.168.XXX.XXX'
PBXL = '192.168.XXX.XXX'
PBXS = '192.168.XXX.XXX'


def peersInfo(name):
    ip = mongo.getOne(name)['PBX']['IP']
    cmd = "asterisk -rx 'sip show peers'"
    peers = ssh.get(ip, cmd)
    for peer in peers:
        print(peer[:-1])


def regInfo(name):
    ip = mongo.getOne(name)['PBX']['IP']
    cmd = "asterisk -rx 'sip show registry '"
    regs = ssh.get(ip, cmd)
    for reg in regs:
        print(reg[:-1])


def dundiInfo(num):
    cmd = f"asterisk -rx 'dundi lookup {num}@priv bypass'"
    numberAdress = ssh.get(DUNDiServer, cmd)
    ip = numberAdress[0][22:-15]
    if len(ip) != 0:
        SName = mongo.getPBX(ip)['Name']
        print(f'{MGA}Number {GRN}{num}{MGA} is on {GRN}{SName}{END}\n'
              f'{MGA}IP:{GRN} {ip}{END}')
    else:
        print(f'{RED}Number {GRN}{num} {RED}is not exist!{END}')


def sipReload(name):
    ip = mongo.getOne(name)['PBX']['IP']
    cmd = "asterisk -rx 'sip reload'"
    ssh.execut(ip, cmd)
    print(f'{MGA}SIP reloaded.{END}')


def dialplanReload(name):
    ip = mongo.getOne(name)['PBX']['IP']
    cmd = "asterisk -rx 'dialplan reload'"
    ssh.execut(ip, cmd)
    print(f'{MGA}Dialpaln reloaded.{END}')


def asteriskRestart(name):
    ip = mongo.getOne(name)['PBX']['IP']
    cmd = "systemctl restart asterisk"
    ssh.execut(ip, cmd)
    print(f'{MGA}Asterisk restarted.{END}')


def startChecking(name):
    cli = ''
    print(f'{MGA}Current status of Asterisk:{END}')
    peersInfo(name)
    regInfo(name)
    while cli != 'exit':
        print(f'{MGA}Available functions:{END}\n'
              f'{MGA}Enter {GRN}1 {MGA}for SIP reload.{END}\n'
              f'{MGA}Enter {GRN}2 {MGA}for Dialplan reload.{END}\n'
              f'{MGA}Enter {GRN}3 {MGA}for Asterisk restart.{END}\n'
              f'{MGA}Enter {GRN}4 {MGA}for get current status.{END}\n'
              f'{MGA}Enter {GRN}exit {MGA}for exit.{END}')
        cli = input(f'{MGA}Enter your choese:{END} ')
        if cli == '1':
            sipReload(name)
        elif cli == '2':
            dialplanReload(name)
        elif cli == '3':
            asteriskRestart(name)
        elif cli == '4':
            peersInfo(name)
            regInfo(name)
        elif cli == 'exit':
            pass
        else:
            print(f'{RED}Try again!{END}')


try:
    startChecking(sys.argv[1])
except KeyboardInterrupt:
    print(f"\n{RED}Exited.{END}")
