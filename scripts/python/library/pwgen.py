#!/usr/bin/python3.6
# -*- coding: utf-8
# Password generator
import random


def account():
    pas = ''
    for x in range(16):
        pas = pas + random.choice(list(f'1234567890abcdefghigklmnopqrstuvyxwz'
                                       f'ABCDEFGHIGKLMNOPQRSTUVYXWZ'))
    secret = pas
    return secret
