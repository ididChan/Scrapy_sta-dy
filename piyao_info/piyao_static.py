from selenium import webdriver
from bs4 import BeautifulSoup
import time

counter = 0

driver = webdriver.Chrome()

driver.get('http://www.xinhuanet.com/food/sppy/qwpy.htm')

title_list = []
title_element = driver.find_elements_by_xpath('//*[@id="showData0"]/li/h3/a')
for item in title_element:
    title_list.append(item.text)
# print(title_list)

content_list = []
content_element = driver.find_elements_by_xpath('//*[@id="showData0"]/li/p')
for ittem in content_element:
    content_list.append(ittem.text)
# print(contents_list)

while counter<10:
    print('【' + title_list[counter]+'】'+content_list[counter]+'\n')
    counter+=1
