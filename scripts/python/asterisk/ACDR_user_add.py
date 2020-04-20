#!/usr/bin/python3.7
# -*- coding: utf-8
# Asterisk-CDR-viewer-mod user add
import sys
from library import pwgen
from library import mail
from library import ssh
from library import mongo


def htpasswd(ip, user, secret):
    order = (f'htpasswd -b '
             f'/var/www/Asterisk-CDR-Viewer-Mod/.htpasswd '
             f'{user} {secret}')
    ssh.execut(ip, order)


def acdr(unit, user, target):
    themes = 'Доступ к АТС. Прослушивание, скачивание аудио записей.'
    secret = pwgen.account()
    ip = mongo.getOne(unit)['PBX']['IP']
    message = (F'IP: {ip}\nLogin: {user}\nPassword: {secret}\n'
               F'Доступно салонам с новыми АТС. Подробности по номеру 1333.')
    htpasswd(ip, user, secret)
    mail.rbt(target, themes, message)


acdr(sys.argv[1], sys.argv[2], sys.argv[3])
