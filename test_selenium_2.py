import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException
import requests
from bs4 import BeautifulSoup
import urllib.request
import csv


driver = webdriver.Chrome()
url = 'https://sadovod.city/category/15'
driver.get(url)
for i in range(2, 11):
    try:
        page = str(i)
        button = driver.find_element_by_link_text(page)
        button.click()
    except TimeoutException:
        print("Box or Button not found in sadovod.city")
    time.sleep(3)
i = 1
page = str(i)
r = requests.get(url).text
soup = BeautifulSoup(r, 'lxml')
table = soup.find('div', class_='product-list clearfix')
items = table.find_all('div', class_='product-item')
i = 1
for item in items:
    number = i
    try:
        title = item.find('div', class_='description-container text-center').find('a').text.strip()
    except:
        title = ''
    try:
        url_g = 'https://sadovod.city' + item.find('div', class_='image-container').find('a').get('href')
    except:
        print(url_g)
    driver.get(url_g)
    time.sleep(3)


