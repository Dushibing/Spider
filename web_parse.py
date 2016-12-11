#_*_coding:utf-8_*_
from bs4 import BeautifulSoup


with open('/Users/dushibing/Downloads/data/data1/Plan-for-combating-master/week1/1_1/1_1answer_of_homework/homework.html','r') as web_data:
    Soup=BeautifulSoup(web_data,'lxml')
    images=Soup.select('html body div.main-content ul.photos li img')
