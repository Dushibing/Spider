from bs4 import BeautifulSoup
import requests
import time

url='https://knewone.com/?page='

def get_url(url):
    header={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:49.0) Gecko/20100101 Firefox/49.0',
            'Cookie':'_knewone_v2_session=bWRZMGJnTmZGakgxaHQraWJqYTVjMEtHN3ZhU290SmlKUkp1WkQ3VFZqcThDSi9HZEc1OUFNc3FrdVN4Q251VHRKV2FaanJDSi9JRnRFRGZUSEZTM3NCYlo0dUpSZmRPbklqK09Vejk2aHZOTXJORkdqdWM3dWZQaEFmTng4ZlVUeFIwZjl6SkhGRlhOT3ZEaHVPNGFCeExqZ2t3OUNsWStBakIrK2lkajZBQmMra1FsWC9PRmFIVnNNb3YyUklaLS1oT3FNZVoxUUFIVmpxUnRQYXRjY0RnPT0%3D--da004bf92f481ab9be122adc871b8fa7eae69d44; _ga=GA1.2.1574853701.1475335585; Hm_lvt_b44696b80ba45a90a23982e53f8347d0=1475335585; Hm_lpvt_b44696b80ba45a90a23982e53f8347d0=1475337423; gr_user_id=f772fe2b-a6a5-42de-a607-641f77c52ebd; gr_session_id_e7b7e334c98d4530928513e7439f9ed2=65c40fa9-8fea-4abc-90c2-c65966eb5dcd; _gat=1'}
    web_data=requests.get(url,headers=header)
    soup=BeautifulSoup(web_data.text,'lxml')
    imgs=soup.select('a.cover-inner > img ')
    titles=soup.select('section.contnet > h4 > a')
    links=soup.select('section.content > h4 > a ')

    for img,title,link in zip(imgs,titles,links):
        data={
            'img':img.get('src'),
            'title':title.get('title'),
            'link':link.get('href')
        }
        print len(data)


def get_more_pages(start,end):
    for one in range(start,end):
        get_url(url+str(one))
        time.sleep(2)


get_more_pages(1,10)