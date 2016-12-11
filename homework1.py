#coding:utf-8
from bs4 import BeautifulSoup
import requests
import time
import random
url='http://zhuanzhuan.58.com/detail/782890936983126020z.shtml'
headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}

def get_links_from(who_sells=0):
    urls=[]
    list_view='http://bj.58.com/pbdn/{}/pn2/'.format(str(who_sells))
    web_data=requests.get(list_view,headers=headers)
    soup=BeautifulSoup(web_data.text,'lxml')
    for link in soup.select('a.t'):
        urls.append(link.get('href').split('?')[0])
    return urls

def get_view_from(url):
    id=url.split('/')[-1].strip('x.shtml')
    api=''

def get_item_info(url):
    web_data=requests.get(url,headers=headers)
    web_data.encoding='utf-8'
    soup=BeautifulSoup(web_data.text,'lxml')
    title=soup.title.text
    content=soup.select('meta[name="description"]')
    price=soup.select('span.price_now > i')
    location=soup.select('div.palce_li > span > i')
    looktime=soup.select('span.look_time')
    want_persion=soup.select('span.want_person')
    data={
        'title':title,
        'content':content[0].text,
        'price':price[0].text,
        'area':location[0].text,
        'looktime':looktime[0].text,
        'wantpersion':want_persion[0].text
    }
    time.sleep(random.randrange(3))
    return data

for url in get_links_from(who_sells=0):
    print get_item_info(url)
