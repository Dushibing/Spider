from bs4 import BeautifulSoup
import requests
import time
import pymongo

client = pymongo.MongoClient('localhost', 27017)
ceshi = client['ceshi']
url_list = ceshi['url_list']
item_info = ceshi['item_info']
header = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
# spider_1

def get_links_from(channel,pages,who_sells=0):
    # http://bj.58.com/shoujihao/0/pn0
    list_view = '{}{}/n{}/'.format(channel, str(who_sells), str(pages))
    web_data = requests.get(list_view)
    time.sleep(1)
    soup = BeautifulSoup(web_data.text, 'lxml')
    if soup.find('td', 't'):
        for link in soup.select('td.t a.t'):
            item_link = link.get('href').split('?')[0]
            # url_list.insert_one({'url': item_link})
            print item_link
    else:
        print 'Last page!'


# get_links_from('http://bj.58.com/shoujihao/',2)

def get_item_info(url):
    wed_data = requests.get(url, headers=header)
    soup = BeautifulSoup(wed_data.text, 'lxml')
    soup.encode_contents(encoding='utf-8')
    no_longer_exitst = '404' in soup.find('script', type='text/javascript').get('src').split('/')
    if no_longer_exitst:
        pass
    else:
        title = soup.title.text
        price = soup.select('span.price.c_f50')[0].text
        print type(price)
        date = soup.select('.time')[0].text
        area = list(soup.select('c_25d a')[0].stripped_strings) if soup.find_all('span', 'c_25d') else None
        # item_info.insert_one({'title': title, 'price': price, 'date': date, 'area': area})
        print {'title': title, 'price': price, 'date': date, 'area': area}

get_item_info('http://bj.58.com/tongxunyw/27559597873965x.shtml')
