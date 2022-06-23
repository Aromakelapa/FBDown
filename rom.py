from bs4 import BeautifulSoup
from time import sleep
import requests
import os


url = input('\nURL Facebook Video : ')
# print(rUrl)

print('\nSilahkan tunggu..')
sleep(1)

rUrl = url.replace('www', 'mbasic', 1)
r = requests.get(rUrl)

print('\nStatus : ', r.status_code)
print()

soup = BeautifulSoup(r.text, 'html.parser').prettify()

try:
    os.mkdir('lib')
except:
    pass
with open('lib/index.html', 'w', encoding = 'UTF-8') as file:
    file.write(soup)
    file.close()

index = open('lib/index.html').read()
scrap = BeautifulSoup(index, 'html.parser')#.div['ca']

linkk = scrap.find('div', 'ca')
src = scrap.find('a')['href']
fSrc = 'https://mbasic.facebook.com' + src
sleep(1)
print('Video Link :\n', fSrc)

def OpenLink(link):
    os.system("termux-open-url \"" + link + "\"")

OpenLink(fSrc)