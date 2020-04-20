#!/usr/bin/env python3.7
# for polybar

import os
import time
import re
import pyperclip
from library import mail

email = pyperclip.paste()
file = f'/home/glitch/Pictures/{time.time()}-scan.png'
subj = 'Скан документа.'
body = (f'Во вложении скан документа.\n\n'
        f'---'
        f'Владислав Ольский.'
        f'Ведущий инженер-программист.'
        f'Телефон: 8(351)XXX-XX-00 доб.1333\n'
        f'Технический отдел.'
        f'Телефон: (351)XXX-XX-01')
cmd = (f'scanimage --buffer-size=1M '
       f'--resolution 300 -x 215 -y 280 '
       f'--mode Gray --format=png > {file}')
if re.search('@', email):
    os.system(cmd)
    mail.XXXAttachment(email, subj, body, file)
else:
    os.system(cmd)
