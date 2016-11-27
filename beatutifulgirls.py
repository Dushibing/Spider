#_*_coding: utf-8 _*_

from bs4 import BeautifulSoup
import requests
import re
import urllib
import os
import random
import time

url='http://jandan.net/ooxx/page-2150#comments'

ippool={
    'http' : '110.16.80.102:8080',
    'https' : '42.53.166.84:8888',
    'htpps' : '42.53.166.84:8888',
}

class ProxieIp(object):
    headers={
        'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:49.0) Gecko/20100101 Firefox/49.0'
    }

    def __init__(self):
        self.url='http://www.data5u.com/'
        self.ippool=[]

    def get_url(self):
        req=requests.get(self.url,self.headers)
        req.encoding='utf-8'
        soup=BeautifulSoup(req.text,'lxml')
        return soup

    def create_pool(self):
        ipinfo=self.get_url()
        ipinfo.encode('utf-8')
        souplist=ipinfo.select('ul.l2 > span > li ')
        iplist=[]
        for i,soup in enumerate(souplist):
            if i % 9 == 0:
                ip=soup.getText()
                port=soup.findNext()
                port=port.getText()
                iplist.append(ip+':'+port)
        with open('proiex','wb') as f :
            for ip in iplist:
                f.write(ip)
                f.write('\n')


class DowloadGirlsImg(object):

    headers={
        'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:49.0) Gecko/20100101 Firefox/49.0'
    }

    def __init__(self):
        os.chdir('img')
        self.data = []
        self.startpagenum = 0
        self.ippool = ippool
        self.starturl = 'http://jandan.net/ooxx/'
        self.currenturl=''


    def GetFirstPageNumber(self):
        req=requests.get(self.starturl,headers=self.headers)
        req.encoding='utf-8'
        soup=BeautifulSoup(req.text,'lxml')
        span=soup.select('span.current-comment-page')
        self.startpagenum=int(str(span[0].get_text())[1:5])

    def get_img_list(self,url):
        req=requests.get(url,headers=self.headers)
        req.encoding='utf-8'
        soup=BeautifulSoup(req.text,'lxml')
        images=soup.select('a.view_img_link')
        for img in images:
            self.data.append(img.get('href'))
        return self.data

    def SaveImag(self,data):
        headers=self.headers
        print data
        if data !=None:
            for url in data:
                filename=url.split('/')[-1]
                urllib.urlretrieve(url,filename)



G=DowloadGirlsImg()
G.GetFirstPageNumber()
for i in range(10):
    G.currenturl=G.starturl+str(G.startpagenum-i)+'#comment'
    data=G.get_img_list(G.currenturl)
    G.SaveImag(data)
