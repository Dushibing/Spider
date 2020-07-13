#_*_coding:utf-8
import urllib2
from bs4 import BeautifulSoup


header = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:49.0) Gecko/20100101 Firefox/49.0'}
	

def getToabaoProdTypeList():
	“”“获取淘宝上面列表”“”
	url = "https://www.taobao.com/"
	request = urllib2.Request(url, headers=header)
	response = urllib2.urlopen(request)
	# print response.read()
	taobao = BeautifulSoup(response,'html.parser')
	bd_list = taobao.find_all('li',class_='J_Cat a-all')
	#for i in range(0,len(bd_list)):
	#	print i, bd_list[i]
	Prodlist={}
	for j in range(0, len(bd_list[0].find_all('a'))):
		item_url = bd_list[j].find_all('a')[j]['href']  # 访问连接
		item_name = bd_list[j].find_all('a')[j].getText()  #条目
		Prodlist[item_name] = item_url
	return Prodlist


def GetProdinsideType(url):
	item_url = url
	request1 = urllib2.Request(item_url, headers=header)
	response1 = urllib2.urlopen(request1)
	item_list = BeautifulSoup(response1,'html.parser')
	item = item_list.find_all('div',class_="xzp-shop-titlemodule J_Module") # xzp-shop-titlemodule J_Module cm-items-oneline6-pc J_Module
	for x in xrange(0,len(item)):
		print item[x].find("span", class_="title-text").getText() # 获取商品细分类成功
	imag_list = item_list.find_all("div",class_="ipic") # 无法一次获取全部的图片，淘宝是基于鼠标上下滑动，动态加载图片，默认值加载六个
	
	
