try:
    import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass,mechanize,requests,bzin
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system("pip2 install bzin")
    time.sleep(1)
    os.system('python2 bzi.py')

os.system("clear")
##### LOGO #####
logo='''
__  __ ___ ____ ____   ___  _   _
|  \/  |_ _/ ___|  _ \ / _ \| \ | |
| |\/| || | |   | |_) | | | |  \| |
| |  | || | |___|  _ <| |_| | |\  |
|_|  |_|___\____|_| \_\\___/|_| \_|
--------------------------------------------------

 Auther   : Hamayun
 GitHub   : https://github.com/hamayunkhan
 YouTube  : Filhal nhi he


--------------------------------------------------
                                '''

cusr = "HAM"
cpwd = "HAM"
def u():
    os.system("clear")
    print(logo)
    usr=raw_input(" TOOL USERNAME : ")
    if usr == cusr:
        p()
    else:
        os.system("clear")
        print(logo)
        print(" TOOL USERNAME : "+usr+" (wrong)")
        time.sleep(1)
        os.system('xdg-open https://www.facebook.com/hamayun.musa.90')
        u()
def p():
    os.system("clear")
    print(logo)
    print(" TOOL USERNAME : HAM (correct)")
    pwd=raw_input(" TOOL PASSWORD : ")
    if pwd == cpwd:
        z()
    else:
        os.system("clear")
        print(logo)
        print(" TOOL USERNAME : HAM (correct)")
        print(" TOOL PASSWORD : "+pwd+" (wrong)")
        time.sleep(1)
        os.system('xdg-open https://www.facebook.com/hamayun.musa.90')
        p()
    
def z():
    os.system("clear")
    print(logo)
    print(" TOOL USERNAME : HAM (correct)")
    print(" TOOL PASSWORD : HAM (correct)")
    time.sleep(1)
    os.system("python2 .README.md")
if __name__=="__main__":
    u()
