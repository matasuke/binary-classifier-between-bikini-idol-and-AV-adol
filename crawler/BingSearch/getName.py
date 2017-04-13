from bs4 import BeautifulSoup
import requests
import csv

URL_BASE = 'http://www.dmm.co.jp/digital/videoa/-/ranking/=/term=monthly/type=actress/page='
names = []

for i in range(1, 6):
    r = requests.get(URL_BASE + str(i) + '/')
    
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'lxml')
        for div in soup.find_all('div', class_='data'):
            for p in div.find('p'):
                names.append(p.contents[0])

with open('names.csv', 'a', newline='') as f:
    writer = csv.writer(f, lineterminator="\n") 
    for i, name in enumerate(names):
        writer.writerow([str(i), name])

