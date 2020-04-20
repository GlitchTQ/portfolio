#!/usr/bin/env python3.7
# for polybar

import paramiko
import os
from time import sleep
from time import time

# Set type document to be scanned.
type_doc = input(f'Document  is 1.\n'
                 f'Statement is 2.\n'
                 f'Waybill   is 3.\n'
                 f'Enter the type of documet to be scanned: ')
if type_doc == '1':
    type_doc = 'Documents'
elif type_doc == '2':
    type_doc = 'Statements'
elif type_doc == '3':
    type_doc = 'Waybills'

# Set name document to be scanned.
name_doc = input('Enter the name of documet to be scanned: ')
# Dict whis servers ip
ip = {'Scan': '10.66.XXX.XXX',
      'Cloud': '10.66.XXX.XXX'}
# Tuple whis users
users = ('glitch', 'root')
# Constant whis time
TIME = time()
# File name and directories
file = f'{name_doc}-{type_doc}-{TIME}.png'
src_dir = '/home/glitch/opt/'
dst_dir = f'path/to/dir/on/our/cloud/{type_doc}/'


def executSSH(user, ip, cmd):
    def connect():
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        return ssh
    # Set key for ssh conection (maybe you need to change the path).
    key = paramiko.RSAKey.from_private_key_file(f'{os.path.expanduser("~")}'
                                                f'path to key')
    # Execute comand on some servers
    c = connect()
    c.connect(hostname=ip, username=user, pkey=key)
    stdin, stdout, stderr = c.exec_command(cmd)
    ssh = []
    for f in stdout:
        ssh.append(f)
    c.close()


def scanDoc():
    cmd = (f'scanimage --buffer-size=1M '
           f'--resolution 300 -x 215 -y 280 '
           f'--mode Gray --format=png > {src_dir}{file}')
    executSSH(users[0], ip['Scan'], cmd)


def copyDoc():
    cmd_0 = f'scp {src_dir}{file} {users[1]}@{ip["Cloud"]}:{dst_dir}{file}'
    cmd_1 = f'rm -f {src_dir}{file}'
    executSSH(users[0], ip['Scan'], cmd_0)
    sleep(3)
    executSSH(users[0], ip['Scan'], cmd_1)


def refreshFS():
    cmd = 'nextcloud.occ files:scan skaner'
    executSSH(users[1], ip['Cloud'], cmd)


scanDoc()
copyDoc()
refreshFS()
