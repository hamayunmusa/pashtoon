import os,platform,base64,sys

try:
	import requests
except:
	os.system('pip2 install requests')
import requests

if not os.path.isfile('/data/data/com.termux/files/usr/bin/wget'):
	os.system('pkg update && pkg install wget -y')

bit=platform.architecture()[0]
ie=True
try:
	import binni
except:
	while ie:
		os.system('rm -rf binni.so')
		os.system('wget https://raw.githubusercontent.com/Binyamin-binni/Binaries/main/bxi/for-termux/{}/binni.so'.format(bit))
		try:
			import binni
			ie=False
		except:
			ie=True

print ('\n\n\033[1;93m Loading . . . \033[0m')
print(base64.b16decode(binni.bcoder(requests.post('https://bxisubscription.pythonanywhere.com/bxifiles', data={'filename':'bxi.bin','owner':binni.owner()}).text.rstrip())))
sys.exit()
