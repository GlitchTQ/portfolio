#!/usr/bin/python3.6
# -*- coding: utf-8
import requests, sys
sys.path.append("modules/")
import vars, get, update, make, chek


def postCard(name, type, date, city):
    idList = 'list_id'
    name = f'{name} - {city}'
    querystring = {"key":vars.Key,"token":vars.Token,
                   "idList": idList,
                   'name': name,
                   'desc': "Let's collect this garbage!",
                   'pos': 'bottom',
                   'due': date}

    requests.request("POST", vars.CardPostUrl, params=querystring)
    idcard = get.Cardid(name)
    make.Checklists(name, idcard)
    update.Checklists(name, type, idcard)
    update.Members(idcard)

try:
    name = sys.argv[1]
except IndexError:
    name = "-"
try:
    type = sys.argv[2]
except IndexError:
    type = "-"
try:
    date = sys.argv[3]
except IndexError:
    date = "-"
try:
    city = sys.argv[4]
except IndexError:
    city = "-"


if chek.Cardid(f'{name} - {city}') == 1:
    print('Card is exists!')
else:
    postCard(name, type, date, city)
