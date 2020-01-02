#!/usr/bin/env python
# _*_encoding:utf-8_*_
"""
@version: ??
@license: Apache Licence 
@site: 
@software: PyCharm
@file: chrome.py
@time: 19/11/12 10:27 AM
"""
__author__ = 'dushibing'
import time
import re
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup

# headers = [["address", "did"]]
# with open('address_did.csv', 'w')as f:
#     f_csv = csv.writer(f)
#     f_csv.writerows(headers)

driver = webdriver.Chrome()
driver.set_page_load_timeout(10)
driver.get("http://www.ynszxc.net/tj/TJ_S.aspx")
s = Select(driver.find_element_by_name("DropDownList_NF"))
s.select_by_value("2010")
elem = driver.find_element_by_css_selector("input[type='radio'][value='5'][name='CKJB']").click()
search = driver.find_element_by_css_selector("input[type='image'][id='ImageButton_Search_01']").click()
result_list = driver.find_element_by_css_selector("a[href='tj_m.aspx?int_PageNum=1']")
driver.execute_script("arguments[0].setAttribute('target','')", result_list)
result_list.click()
for i in range(1, 1223):
    soup = BeautifulSoup(driver.page_source, "lxml")
    table_node = soup.find_all("table")
    rows = table_node[5].findAll("tr")
    pagelist = [
        [rows[2].get_text().encode("utf-8"), re.findall(r'\d{3,8}', rows[2].a.attrs['href'])[0]],
        [rows[3].get_text().encode("utf-8"), re.findall(r'\d{3,8}', rows[3].a.attrs['href'])[0]],
        [rows[4].get_text().encode("utf-8"), re.findall(r'\d{3,8}', rows[4].a.attrs['href'])[0]],
        [rows[5].get_text().encode("utf-8"), re.findall(r'\d{3,8}', rows[5].a.attrs['href'])[0]],
        [rows[6].get_text().encode("utf-8"), re.findall(r'\d{3,8}', rows[6].a.attrs['href'])[0]],
        [rows[7].get_text().encode("utf-8"), re.findall(r'\d{3,8}', rows[7].a.attrs['href'])[0]],
        [rows[8].get_text().encode("utf-8"), re.findall(r'\d{3,8}', rows[8].a.attrs['href'])[0]],
        [rows[9].get_text().encode("utf-8"), re.findall(r'\d{3,8}', rows[9].a.attrs['href'])[0]],
        [rows[10].get_text().encode("utf-8"), re.findall(r'\d{3,8}', rows[10].a.attrs['href'])[0]],
        [rows[11].get_text().encode("utf-8"), re.findall(r'\d{3,8}', rows[11].a.attrs['href'])[0]],
        ]
    with open('address_did.csv', 'ab+')as f:
        f_csv = csv.writer(f)
        f_csv.writerows(pagelist)
    PageNum = rows[12].get_text().encode("utf-8").split(' ')[5]
    next = driver.find_element_by_css_selector("a[href='tj_m.aspx?int_PageNow={0}']".format(str(int(PageNum)+1)))
    next.click()
    time.sleep(0.5)
driver.close()

# /Users/dushibing/PycharmProjects/NativePython/address_did.csv
