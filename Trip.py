#_*_coding:utf-8_*_
from bs4 import BeautifulSoup
import requests
import time
url='http://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html'
urls=['http://www.tripadvisor.com/Attractions-g60763-Activities-oa{}-New_York_City_New_York.html#ATTRACTION_LIST'.format(str(i)) for i in range(30,930,30)]

headers={
    'User-Agent':'Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
}
def get_favs(url):
    web_data=requests.get(url,headers=headers)
    time.sleep(1)
    soup=BeautifulSoup(web_data.text,'lxml',from_encoding="utf8")
    print soup
    titles=soup.select('div.property_title > a[target="_blank"]')
    images=soup.select('div.photo_booking > img[width="160"]')
    cates=soup.select('div.p13n_reasoning_v2')
    for title,img,cate in zip(titles,images,cates):
        data={
            'title':title.get_text(),
            'img':img.get('src'),
            'cate':list(cate.stripped_strings),
        }
        print data
for url in urls:
    get_favs(url)
