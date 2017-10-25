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
import json
import urllib.parse

# Не работает. Затыкается на 28 строке.

def init_driver():
    driver = webdriver.Chrome()
    driver.wait = WebDriverWait(driver, 5)
    return driver

def get_html(url, page):
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'lxml')
    return soup

def get_wd(url, page):
    if page == 1:
        r = requests.get(url).text
        soup = BeautifulSoup(r, 'lxml')
    else:
        driver = init_driver()
        (driver.get(url))
        page = str(page)
        button = driver.find_element_by_link_text(page)
        button.click()
        time.sleep(6)
        r = driver.page_source
        soup = BeautifulSoup(r, 'lxml')
    return soup
#                                Добавлено вычисление последней страницы
def write_csv(data):
    with open('sadovod.csv', 'a') as f:
        writer = csv.writer(f, delimiter=';', lineterminator='\n')
        writer.writerow( (data['number'], data['article'], data['title'], data['price'], data['sizes'], data['color'], data['facture'], data['date'], data['url']) )

def get_total_pages(soup):
        t_pages = soup.find('ul', class_='pagination').find_all('a')[-1].get('data-ci-pagination-page')
        return int(t_pages)

def parse(soup):
    table = soup.find('div', class_='product-list clearfix')
    items = table.find_all('div', class_='product-item')
    # print(items)
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
            url_g = ''
        try:
            article = url_g.split('/')[4]
        except:
            url_g = ''
        try:
            price = item.find('div', class_='price-container text-right').text.strip()
        except:
            price = ''
                           # Краулер: Переходим на страницу каждого товара, чтобы получить размеры и цвета.
        soup = get_html(url_g, 1)
        table_2 = soup.find('div', class_='combinations')
        try:
            sizes = table_2.find('div', class_='select col-md-6 col-sm-9').find('select').text.strip()
        except:
            sizes = ''
        try:
            color = table_2.find('div', class_='product-colors form-group').find('select').text.strip()
        except:
            color = ''
        try:
            facture = table_2.find('div', class_='product-tkan form-group').find('p').text.strip()
        except:
            facture = ''
        try:
            pdate = table_2.find('div', class_='product-price form-group').text.strip()
            date = pdate.split(':')[2].split(' ')[1]
        except:
            date = ''
        data = {'number':number,
                'article':article,
                'title':title,
                'price':price,
                'sizes':sizes,
                'color':color,
                'facture':facture,
                'date':date,
                'url':url_g}
        write_csv(data)
        i += 1


def main():
    url = 'https://sadovod.city/category/66'
    total_pages = get_total_pages(get_html(url, 1))
    for i in range(1, total_pages):
        print(i)
        parse(get_wd(url, i))
    # driver.quit()


if __name__ == '__main__':
    main()