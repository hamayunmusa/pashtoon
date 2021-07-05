# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Mar 20 2021, 14:59:33) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: aso
import os, sys, time, datetime, re, threading, json, random, requests, hashlib, cookielib, uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
__author__ = 'Zubair Zubi'
__copyright = 'All rights reserved . Copyright  Zubair Zubi'
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
CorrectUsername = 'WELCOME'
loop = 'true'
while loop == 'true':
    username = raw_input('\x1b[1;91m\x1b[1;91mENTER KEY : \x1b[1;91m \x1b[1;91m')
    if username == CorrectUsername:
        print '\x1b[1;92mActivated '
        time.sleep(5)
        loop = 'false'

<?php
   session_start(); 
?>
<html xmlns:fb = "http://www.facebook.com/2008/fbml">
   
   <head>
      <title>Login with Facebook</title>
      <link 
         href = "http://www.bootstrapcdn.com/twitter-bootstrap/2.2.2/css/bootstrap-combined.min.css" 
         rel = "stylesheet">
   </head>
   
   <body>
      <?php if ($_SESSION['FBID']): ?>      <!--  After user login  -->
         
         <div class = "container">
            
            <div class = "hero-unit">
               <h1>Hello <?php echo $_SESSION['USERNAME']; ?></h1>
               <p>Welcome to "facebook login" tutorial</p>
            </div>
            
            <div class = "span4">
				
               <ul class = "nav nav-list">
                  <li class = "nav-header">Image</li>
						
                  <li><img src = "https://graph.facebook.com/<?php 
                     echo $_SESSION['FBID']; ?>/picture"></li>
                  
                  <li class = "nav-header">Facebook ID</li>
                  <li><?php echo  $_SESSION['FBID']; ?></li>
               
                  <li class = "nav-header">Facebook fullname</li>
						
                  <li><?php echo $_SESSION['FULLNAME']; ?></li>
               
                  <li class = "nav-header">Facebook Email</li>
						
                  <li><?php echo $_SESSION['EMAIL']; ?></li>
               
                  <div><a href="logout.php">Logout</a></div>
						
               </ul>
					
            </div>
         </div>
         
         <?php else: ?>     <!-- Before login --> 
         
         <div class = "container">
            <h1>Login with Facebook</h1>
            Not Connected
            
            <div>
               <a href = "fbconfig.php">Login with Facebook</a>
            </div>
            
            <div>
               <a href = "http://www.tutorialspoint.com"  
                  title = "Login with facebook">More information about Tutorialspoint</a>
            </div>
         </div>
         
      <?php endif ?>
      
   </body>
</html>        
