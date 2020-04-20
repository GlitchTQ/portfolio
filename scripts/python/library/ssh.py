#!/usr/bin/python3.6
# -*- coding: utf-8
import paramiko

key = paramiko.RSAKey.from_private_key_file("path to key")


def connect():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    return ssh


def get(ip, cmd):
    c = connect()
    c.connect(hostname=ip, username='root', pkey=key)
    stdin, stdout, stderr = c.exec_command(cmd)
    ssh = []
    for f in stdout:
        ssh.append(f)
    c.close()
    return ssh


def gw_get(ip, cmd):
    c = connect()
    c.connect(hostname=ip, username='root', pkey=key, port=222)
    stdin, stdout, stderr = c.exec_command(cmd)
    ssh = []
    for f in stdout:
        ssh.append(f)
    c.close()
    return ssh


def execut(ip, cmd):
    c = connect()
    c.connect(hostname=ip, username='root', pkey=key)
    c.exec_command(cmd)
    c.close()


def copy(ip, src, dst):
    t = paramiko.Transport(ip, 22)
    t.connect(username='root', pkey=key)
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.put(src, dst)
    sftp.close()
    t.close()
