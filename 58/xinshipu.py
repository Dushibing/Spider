# _*_coding:utf-8_*_
# __author__ = 'dushibing'

from bs4 import  BeautifulSoup
import requests


head = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
url = 'http://www.xinshipu.com/zuofa/49391'
req = requests.get(url, headers=head)
soup = BeautifulSoup(req.text, 'lxml')
title = soup.select('.re-up h1')[0].text
cailiao = soup.select('.dd')[0].text
zuofa=[]
for child in soup.select('.dd')[1].children:
    if len(child.string) > 10:
        zuofa.append(child.string)

print ','.join(zuofa)
