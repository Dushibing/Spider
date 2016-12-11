# coding:utf-8
from bs4 import BeautifulSoup
import requests
import time
import pymongo

client = pymongo.MongoClient('localhost', 27017)
gphonenum=client['gohonenum']
phoneinfo=gphonenum['phoneinfo']

header = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}


def get_phone_number(url):
    req = requests.get(url,headers=header)
    req.encoding = 'utf-8'
    soup = BeautifulSoup(req.text, 'lxml')
    soup.decode('unicode')
    phone_numbers = soup.select('.number')
    price_list = soup.select('.price')

    for phone_number, price in zip(phone_numbers, price_list):
        data = {
            'number': phone_number.text,
            'price': price.text
        }
        phoneinfo.insert_one(data)
    time.sleep(1)


def get_all_phone():
    url = 'http://bj.58.com/shoujihao/pn{}'
    for i in range(12):
        url=url.format(i)
        get_phone_number(url)

get_all_phone()