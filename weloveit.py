#_*_coding:utf-8
from bs4 import BeautifulSoup
import requests
import os
import urllib
import random
import time
import threading


header = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:49.0) Gecko/20100101 Firefox/49.0'}

proxie={
    'https' : '119.2.77.1:8080',
    'https' : '125.163.172.7:8080',
}

url = 'http://weheartit.com/inspirations/beauty?page={}'

def get_url(url):
    req = requests.get(url, headers=header,proxies=proxie)
    req.encoding = 'utf-8'
    soup = BeautifulSoup(req.text, 'lxml')
    images = soup.select('img.entry-thumbnail')
    publishs = soup.select('span.text-overflow > a > span.text-big')
    data = {}
    for publish ,img in zip(publishs , images):
        name = publish.get_text()
        data[name] = img.get('src')
    return data

def save_img(data):
    if data != None:
        for key in data:
            with open('imgs/'+key+str(random.randrange(1000))+'.jpg','wb') as f:
                content=urllib.urlopen(data[key]).read()
                f.write(content)
    time.sleep(1)

if __name__ == '__main__':
    for i in range(10,20):
        data = get_url(url.format(i))
        t = threading.Thread(target=save_img, args=(data, ))
        t.start()

