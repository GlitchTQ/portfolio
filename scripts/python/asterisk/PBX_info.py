#!/usr/bin/env python3.7
# -*- coding: utf-8

import colorama
from library import ssh


colorama.init()
RED = colorama.Fore.RED
GRN = colorama.Fore.GREEN
BLE = colorama.Fore.BLUE
MGA = colorama.Fore.MAGENTA
END = colorama.Style.RESET_ALL

IP = '192.168.XXX.XXX'


def freeNumbers():
    cmd = (f"asterisk -rx 'sip show peers' "
           f"| awk '/^7/ && /Unspecified/ {{print $1}}'")
    result = ssh.get(IP, cmd)
    for len in result:
        print(len[:-1])


def showUser(name):
    cmd = f"asterisk -rx 'sip show peers' | egrep {name}"
    result = ssh.get(IP, cmd)
    cmd2 = (f"grep -E '[[:digit:]]{{4}}' "
            f"/etc/asterisk/template/sip/{name}_users.conf"
            f"| awk NR==1'{{print $2}}'")
    localNum = ssh.get(IP, cmd2)
    try:
        print(f'{MGA}Number of subdivision:{GRN} {localNum[0][1:-2]}{END}')
    except IndexError:
        print(f'{RED}Unit not configured or not standard configured{END}')
        raise SystemExit()
    print(f'{MGA}SIP users info:{END}')
    for len in result:
        print(f'{len[:-1]}')


print((f'{MGA}Choose:\n'
       f'Free numbers: {GRN}1\n'
       f'{MGA}Show unit data: {GRN}2{END}'))
choose = input(f'{MGA}Your choose: {END}')
if choose == '1':
    freeNumbers()
elif choose == '2':
    unit = input(f'{MGA}Enter the subdivision number:{END} ')
    showUser(unit)
else:
    print(f'{RED}Something went wrong{END}')
