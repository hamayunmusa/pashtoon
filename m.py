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
logo = '\n\x1b[1;93m=\xc2\xb0=\xc2\xb0=> ######## ##     ## ########  #### <=\xc2\xb0=\xc2\xb0=\n\x1b[1;92m=\xc2\xb0=\xc2\xb0=>      ##  ##     ## ##     ##  ##  <=\xc2\xb0=\xc2\xb0=\n\x1b[1;93m=\xc2\xb0=\xc2\xb0=>     ##   ##     ## ##     ##  ##  <=\xc2\xb0=\xc2\xb0=\n\x1b[1;92m=\xc2\xb0=\xc2\xb0=>    ##    ##     ## ########   ##  <=\xc2\xb0=\xc2\xb0=\n\x1b[1;93m=\xc2\xb0=\xc2\xb0=>   ##     ##     ## ##     ##  ##  <=\xc2\xb0=\xc2\xb0=\n\x1b[1;92m=\xc2\xb0=\xc2\xb0=>  ##      ##     ## ##     ##  ##  <=\xc2\xb0=\xc2\xb0=\n\x1b[1;93m=\xc2\xb0=\xc2\xb0=> ########  #######  ########  #### <=\xc2\xb0=\xc2\xb0=\n\x1b[1;96m-----------------------------------------------\n\x1b[1;93m\xe2\x9e\xa3 \x1b[1;92mPROGRAMER   \x1b[1;93m: \x1b[1;92mHAMAYUN KHAN\n\x1b[1;93m\xe2\x9e\xa3 \x1b[1;92mFACEBOOK    \x1b[1;93m: \x1b[1;92mHAMAYUN KHAN\n\x1b[1;93m\xe2\x9e\xa3 \x1b[1;92mWHATSAPP    \x1b[1;93m: \x1b[1;92m03319258250 \n\x1b[1;96m-----------------------------------------------'
print logo
CorrectUsername = 'HELLO'
loop = 'true'
while loop == 'true':
    username = raw_input('\x1b[1;91m\x1b[1;91mENTER KEY : \x1b[1;91m \x1b[1;91m')
    if username == CorrectUsername:
        print '\x1b[1;92mActivated '
        time.sleep(5)
        loop = 'false'
        
def log_menu():
    try:
        t_check = open('access_token.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\x1b[1;96m-----------------------------------------------'
        print '\x1b[1;93m[1] \x1b[1;92mLogin With Facebook'
        print '\x1b[1;93m[2] \x1b[1;92mLogin With Token'
        print '\x1b[1;93m[3] \x1b[1;92mLogin With Cookies'
        print '\x1b[1;96m-----------------------------------------------'
        log_menu_s()


def log_menu_s():
    s = raw_input('\x1b[1;93m\xe2\x8c\x90\xe2\x95\xa6\xe2\x95\xa6\xe2\x95\x90\xe2\x94\x80 ')
    if s == '1':
        log_fb()
    elif s == '2':
        log_token()
    elif s == '3':
        log_cookie()
    else:
        print ''
        print '\\ Select valid option '
        print ''
        log_menu_s()


def log_fb():
    os.system('clear')
    print logo
    print '\x1b[1;31;1mLogin with id/pass'
    print '\x1b[1;96m-----------------------------------------------'
    lid = raw_input('\x1b[1;92m Id/mail/no: ')
    pwds = raw_input(' \x1b[1;93mPassword: ')
    try:
        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pwd).text
        q = json.loads(data)
        if 'loc' in q:
            ts = open('access_token.txt', 'w')
            ts.write(q['loc'])
            ts.close()
            menu()
        elif 'www.facebook.com' in q['error']:
            print ' User must verify account before login'
            raw_input('\x1b[1;92m Press enter to try again ')
            log_fb()
        else:
            print ' Id/Pass may be wrong'
            raw_input(' \x1b[1;92mPress enter to try again ')
            log_fb()
    except:
        print ''
        print 'Exiting tool'
        os.system('exit')


def log_token():
    os.system('clear')
    print logo
    print '\x1b[1;93mLogin with token\x1b[1;91m'
    print '\x1b[1;96m-----------------------------------------------'
    tok = raw_input('\x1b[1;92mPaste Token Here : \x1b[1;91m')
    print '\x1b[1;96m-----------------------------------------------'
    t_s = open('access_token.txt', 'w')
    t_s.write(tok)
    t_s.close()
    menu()
