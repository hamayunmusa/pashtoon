# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Mar 20 2021, 14:59:33) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: aso
import os, sys, time, datetime, re, threading, json, random, requests, hashlib, cookielib, uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
__author__ = 'HAMAYUN KHAN'
__copyright = 'All rights reserved . Copyright  Hamayun'
os.system('pkg install nodejs')
try:
    os.mkdir('/sdcard/ids')
except OSError:
    pass

bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000, 40000)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 
   'x-fb-net-hni': repr(sim), 
   'x-fb-connection-quality': 'EXCELLENT', 
   'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
   'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]', 
   'content-type': 'application/x-www-form-urlencoded', 
   'x-fb-http-engine': 'Liger'}
os.system('git pull')
os.system('clear')
logo = '\n\x1b[1;93m=\xc2\xb0=\xc2\xb0=> ######## ##     ## ########  #### <=\xc2\xb0=\xc2\xb0=\n\x1b[1;92m=\xc2\xb0=\xc2\xb0=>      ##  ##     ## ##     ##  ##  <=\xc2\xb0=\xc2\xb0=\n\x1b[1;93m=\xc2\xb0=\xc2\xb0=>     ##   ##     ## ##     ##  ##  <=\xc2\xb0=\xc2\xb0=\n\x1b[1;92m=\xc2\xb0=\xc2\xb0=>    ##    ##     ## ########   ##  <=\xc2\xb0=\xc2\xb0=\n\x1b[1;93m=\xc2\xb0=\xc2\xb0=>   ##     ##     ## ##     ##  ##  <=\xc2\xb0=\xc2\xb0=\n\x1b[1;92m=\xc2\xb0=\xc2\xb0=>  ##      ##     ## ##     ##  ##  <=\xc2\xb0=\xc2\xb0=\n\x1b[1;93m=\xc2\xb0=\xc2\xb0=> ########  #######  ########  #### <=\xc2\xb0=\xc2\xb0=\n\x1b[1;96m-----------------------------------------------\n\x1b[1;93m\xe2\x9e\xa3 \x1b[1;92mPROGRAMER   \x1b[1;93m: \x1b[1;92mZUBAIR ZUBI\n\x1b[1;93m\xe2\x9e\xa3 \x1b[1;92mFACEBOOK    \x1b[1;93m: \x1b[1;92mUSMAN ULLAH\n\x1b[1;93m\xe2\x9e\xa3 \x1b[1;92mWHATSAPP    \x1b[1;93m: \x1b[1;92mMAI NAHI BATAONGA \n\x1b[1;96m-----------------------------------------------'
print logo
CorrectUsername = 'HELLO'
loop = 'true'
while loop == 'true':
    username = raw_input('\x1b[1;91m\x1b[1;91mENTER KEY : \x1b[1;91m \x1b[1;91m')
    if username == CorrectUsername:
        print '\x1b[1;92mActivated '
        time.sleep(5)
        loop = 'false'