#!/usr/bin/env python
# _*_encoding:utf-8_*_
"""
@version: ??
@license: Apache Licence 
@site: 
@software: PyCharm
@file: chome2.py
@time: 19/11/29 5:16 PM
"""
__author__ = 'dushibing'

import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup


# 解析表格数据
def dataTable(address, didnum, rows,  pagelist, year):
    i = 1
    for row in rows:
        if i == 1:
            pagelist.append([address, didnum, year, row.findAll("td")[2].get_text().encode("utf-8").replace("\n", ""), row.findAll("td")[3].get_text().encode("utf-8").replace("\n", ""), row.findAll("td")[4].get_text().encode("utf-8").replace("\n", "")])
        else:
            pagelist.append([address, didnum, year, row.findAll("td")[1].get_text().encode("utf-8").replace("\n", ""), row.findAll("td")[2].get_text().encode("utf-8").replace("\n", ""), row.findAll("td")[3].get_text().encode("utf-8").replace("\n", "")])
        i = i + 1
    return pagelist

#解析不规则表格数据
def lastTable(address, didnum, rows,  pagelist, year):
    i = 1
    for row in rows:
        if i == 1:
            pagelist.append([address, didnum, year, "发展重点 1", ' ', row.findAll("td")[2].get_text().encode("utf-8").replace("\n", "")])
        else:
            pagelist.append([address, didnum, year, "发展重点 2", ' ', row.findAll("td")[1].get_text().encode("utf-8").replace("\n", "")])
        i = i + 1
    return pagelist

#写入数据到csv文件
def get_cpuntry_inforamtion(address, didnum):
    driver.get("http://www.ynszxc.net/report/default.aspx?departmentid={0}".format(didnum))
    elem = driver.find_element_by_name("ddlYear")
    print elem.text
    for selectyear in elem.text.encode("utf-8").replace(" ", "").split('\n'):
        s = Select(driver.find_element_by_name("ddlYear"))
        s.select_by_value(selectyear)
        soup = BeautifulSoup(driver.page_source, "lxml")
        table_nodes = soup.find_all("table")
        pagelist = []
        for i in range(1, len(table_nodes)-1):
            rows = table_nodes[i].findAll("tr")
            dataTable(address, didnum, rows, pagelist, selectyear)
        lastTable(address, didnum, table_nodes[10].findAll("tr"), pagelist, selectyear)
        # 这里文件名 country_information.csv 为抓取信息的写入文件，文件如果不存在程序会自动创建
        with open('country_information.csv', 'ab+')as f:
            f_csv = csv.writer(f)
            f_csv.writerows(pagelist)
        time.sleep(0.5)

chrome_options = Options()
chrome_options.add_argument('--incognito')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--hide-scrollbars')
chrome_options.add_argument('blink-settings=imagesEnabled=false')
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(options=chrome_options)
driver.set_page_load_timeout(10)

# 这里的address_did1.csv 文件为获取did number的文件，如果文件名有变化，修改这里文件名
with open('address_did1.csv', 'r') as f:
    reader = csv.reader(f)
    didList = [row for row in reader]
    i = 0
    for country in didList:
        if i == 0:
            print country[0], country[1]
            i = i + 1
        else:
            try:
                get_cpuntry_inforamtion(country[0], country[1])
            except Exception, err:
                print err
            i = i + 1

driver.close()

