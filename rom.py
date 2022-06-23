from bs4 import BeautifulSoup
from time import sleep
import requests
import os


url = input('URL Facebook Video : ')
# print(rUrl)

print('Silahkan tunggu..')
sleep(1)

rUrl = url.replace('www', 'mbasic', 1)
r = requests.get(rUrl)

print('Status : ' + r.status.code)
print()

soup = BeautifulSoup(r.text, 'xml').prettify()

try:
    os.mkdir('lib')
except:
    pass
with open('lib/index.html', encoding = 'UTF-8') as file:
    file.write(soup)
    file.close()

index = open('lib/index.html').read()
scrap = BeautifulSoup(index, 'xml')

__link__ = scrap.find('div', 'ca')
src = __link__.find('a')['href']

sleep(1)
print('Video Link :\n', src)

def OpenLink(link):
    os.system("termux-open-url \"" + link + "\"")

OpenLink(src)