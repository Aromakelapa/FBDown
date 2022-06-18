import requests
import os
from time import sleep
from bs4 import BeautifulSoup

inputt = input('URL facebook : ')
split1 = inputt.split('/')
# print(split1)
split2 = split1[2].split('.')
# print(split2)
replace1 = split2[0].replace('www', 'mbasic')
# print(replace1)
slash = '/'
d = '.'
s = str(slash)
overall = split1[0]+s+s + split1[1] + replace1+d + split2[1]+d + split2[2]+s + split1[3]+s + split1[4]+s + split1[5]+s + split1[6]
# print(overall)
print('\nSilahkan tunggu..\n')
sleep(1)
url = overall
r = requests.get(url)
print('Status : ', r.status_code)
print()
# print(r.text)

soup = BeautifulSoup(r.text, 'xml').prettify()

with open('index.html', 'w', encoding='utf-8') as file:
	file.write(soup)
	file.close()

index = open('index.html').read()

scrap = BeautifulSoup(index, 'xml')

linkk = scrap.find('div', 'ca')

src = linkk.find('a')['href']

asu = 'http://mbasic.facebook.com' + src

sleep(2)
print('Video Link :\n\n',asu)

def OpenLink(link):
	os.system("termux-open-url \""+link+"\"")

OpenLink(asu)
