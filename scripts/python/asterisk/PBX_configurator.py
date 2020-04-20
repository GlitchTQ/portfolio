#!/usr/bin/python3.6
# -*- coding: utf-8
#Local context generator

# deprecated

import sys, os, re
sys.path.append("/home/glitch/script/python/library/")
import db_work, ssh, reach, mongo, TrunkInfoUpdate



#DUNDi
def dundi(num, ip):
    DUNDi_ip = '192.168.XXX.XXX'
    DUNDi_dir = '/etc/asterisk/dundi_peers/S{}.conf'.format(num)
    Rconf = os.path.join('/home/glitch/script/python/temp/dundi_files/',
                        'Rdundi_S{}.conf'.format(num))
    dcon = os.path.join('/home/glitch/script/python/temp/dundi_files/',
                         'Sdundi_S{}.conf'.format(num))
    iax = os.path.join('/home/glitch/script/python/temp/dundi_files/',
                       'iax.conf')

    mac_list = ssh.get(ip, 'ip a')

    for mac_line in mac_list:
        if re.search(r'link/ether', mac_line):
            #print(mac_line)
            mac = (mac_line.split(' '))[5]
            print(F'UNIT = {num} \nIP = {ip} \nMAC = {mac}')

    config = ('[general]', F'department = S{num}', 'organization = XXX.RU',
              'locality = Chelabinsk', 'stateprov = CHE', 'country = RU',
              'email = root@localhost', 'phone = 1333', ' ',
              'bindaddr = 0.0.0.0', 'port = 4520', F'entityid = {mac}',
              'ttl = 5', 'autokill = 4000', 'cachetime = 600',
              'secretpath = dundi', ' ', '[mappings]',
              F'priv => local,0,IAX2,dundi@{ip}/${{NUMBER}},nopartial', ' ',
              '[10:50:56:81:43:12]', 'model = symmetric',
              'host = 192.168.98.13', 'inkey =', 'outkey =', 'include = priv',
              'permit = priv', 'qualify = yes', 'order = primary')

    dundi_conf = (F'[{mac}] ; S{num}', 'model = symmetric',
                  F'host = {ip}', 'inkey =', 'outkey =',
                  'include = priv', 'permit = priv', 'qualify = no',
                  'order = primary')

    with open(Rconf, 'w+', encoding='UTF-8') as f:
        for line in config:
            f.write(line + '\n')

    with open(dcon, 'w+', encoding='UTF-8') as f:
        for line in dundi_conf:
            f.write(line + '\n')
    #Copying a DUNDi configuration to a remote host
    ssh.copy(ip, Rconf, '/etc/asterisk/dundi.conf')
    #Copying a IAX configuration to a remote host
    ssh.copy(ip, iax, '/etc/asterisk/iax.conf')
    #Copying a DUNDi configuration to a DUNDi server
    ssh.copy(DUNDi_ip, dcon, DUNDi_dir)
    print('Create DUNDi connection finished.')


#Extensions
def Outgoing(unit, ip):
    path = os.path.join('/home/glitch/script/python/temp/',
                        'out_{}.conf'.format(unit))
    dst = os.path.join('/etc/asterisk/template/exten/',
                        'out.conf')
    with open(path, 'w+', encoding='UTF-8') as f:
        f.write('[out-city]\n')
    context = ('include => conf_user_add',
               'include => in-company',
               'ignorepat => 9',
               'exten => _9.,1,NoOp(Городской вызов на ${EXTEN})',
               ' same => n,Macro(recording,${CALLERID(num)},${EXTEN}))',
               f' same => n,Dial(SIP/{unit}/${{EXTEN:1}},60,T)',
               ' same => n(blacklist),Playback(ru/tt-weasels)',
               ' same => n(end),HangUp()')
    with open(path, 'a', encoding='UTF-8') as f:
        for line in context:
            f.write(line + '\n')
    ssh.copy(ip, path, dst)
    print('Create Outgoing context finished.')


def incoming(unit, number, exten, ip):
    path = os.path.join('/home/glitch/script/python/temp/',
                        'in_{}.conf'.format(number))
    dst = os.path.join('/etc/asterisk/template/exten/',
                        'in.conf')
    with open(path, 'w+', encoding='UTF-8') as f:
        f.write('[in-city]\n')
    context = (f'exten => {number},1,Answer()',
               ' same => n,GotoIf($[${BLACKLIST()}=1]?blacklist)',
               ' same => n,Macro(dev-stat,${EXTEN})',
               ' same => n,Macro(recording,${CALLERID(num)},${EXTEN})',
               f' same => n,Dial(SIP/{exten},60,tm)',
               ' same => n,Goto(end)',
               ' same => n(blacklist),Playback(ru/tt-weasels)',
               ' same => n(end),HangUp()')
    with open(path, 'a', encoding='UTF-8') as f:
        for line in context:
            f.write(line + '\n')
    ssh.copy(ip, path, dst)
    print('Create Incoming context finished.')


def local(unit, number, ip):
    count = 10
    number = int(number)
    path = os.path.join('/home/glitch/script/python/temp/',
                        'local_{}.conf'.format(number))
    dst = os.path.join('/etc/asterisk/template/exten/',
                        'local.conf')
    with open(path, 'w+', encoding='UTF-8') as f:
        f.write('[local]\n')
    while count > 0:
        context = (f'exten => {number},1,NoOp(Call for {number})',
                   ' same => n,Macro(recording,${CALLERID(num)},${EXTEN})',
                   f' same => n,Dial(SIP/{number},30,Tt)',
                   ' same => n,HangUp()')
        with open(path, 'a', encoding='UTF-8') as f:
            for line in context:
                f.write(line + '\n')
        number = number + 1
        count = count - 1
    ssh.copy(ip, path, dst)
    print('Create Local context finished.')


#SIP
def sip_users(unit, number, ip):
    count = 10
    number = int(number)
    MASK = {'PBX.MASK': f'{str(number)[:-1]}X'}
    path = os.path.join('/home/glitch/script/python/temp/',
                        f'sip_users_{str(number)[:-1]}X.conf')
    dst = os.path.join('/etc/asterisk/template/sip/',
                        f'users_{str(number)[:-1]}X.conf')
    while count > 0:
        user = (f'[{number}](salon)',
                f'callerid = {number} <{number}>',
                f'secret   = {number}XXX',
                 'context  = in-company')
        with open(path, 'a', encoding='UTF-8') as f:
            for line in user:
                f.write(line + '\n')
        number = number + 1
        count = count - 1
    ssh.copy(ip, path, dst)
    mongo.update(unit, MASK)
    print('Create SIP users finished.')


def sip_trunk(unit, number, pas, auth, host, ip):
    path = os.path.join('/home/glitch/script/python/temp/',
                        'sip_trunk_{}.conf'.format(number))
    dst = os.path.join('/etc/asterisk/template/sip/',
                       'trunk_{}.conf'.format(number))
    reg_string = os.path.join('/etc/asterisk/',
                       'sip_regstring.conf'.format(number))
    trunk = (f'[{unit}](out.sample)',
             f'defaultuser = {number}',
             f'fromuser    = {number}',
             f'secret      = {pas}',
             f'host        = {host}',
             f'fromdomain  = {host}',
             'nat         = force_rport,comedia')
    reg = f"register={number}:{pas}:{auth}@{host}/{number}"
    with open(path, 'w', encoding='UTF-8') as f:
        for line in trunk:
            f.write(line + '\n')
    cmd = f"echo '{reg}' >> {reg_string}"
    ssh.execut(ip, cmd)
    ssh.copy(ip, path, dst)
    if host[-5:] == 'rt.ru':
        type = 'vATC'
    else:
        type = 'Trunk'
    TrunkInfoUpdate.work(unit, type, host, number, auth, pas)
    print('Create SIP trunk finished.')


def start(unit):
    print('Start building PBX configuration.')
    s = input('Full configuration? (y/n): ')

    if s == 'y':
        number = input('Enter the first local number: ')
        lend_num = input('Enter the lendline number: ')
        pas = input('Enter the lendline password: ')
        auth = input('Enter lendline number of subdivision: ')
        host = input('Enter the host of lendline number: ')
        sip_users(unit, number, ip)
        sip_trunk(unit, lend_num, pas, auth, host, ip)
        local(unit, number, ip)
        dundi(unit, ip)
        incoming(unit, lend_num, number, ip)
        Outgoing(unit, ip)
    elif s == 'n':
        s = int(input('Creating users: 1\n' +
                      'Creating DUNDi link: 2\n' +
                      'Creating trunk: 3\n' +
                      'Creating city context: 4\n' +
                      'Enter your selection: '))
        if s == 1:
            number = input('Enter the first local number: ')
            sip_users(unit, number, ip)
            local(unit, number, ip)
        elif s == 2:
            dundi(unit, ip)
        elif s == 3:
            lend_num = input('Enter the lendline number: ')
            pas = input('Enter the lendline password: ')
            auth = input('Enter the authorized landline number: ')
            host = input('Enter the host of lendline number: ')
            sip_trunk(unit, lend_num, pas, auth, host, ip)
        elif s == 4:
            exten = input('Local number: ')
            number = input('Lendline number: ')
            Outgoing(unit, ip)
            incoming(unit, number, exten, ip)
        else:
            print('Wrong data')
            start(unit)
    else:
        print('Wrong data')
        start(unit)

unit = input('Enter the subdivision number: ')
ip = mongo.getOne(unit)['PBX']['IP']
print(ip)
start(unit)
