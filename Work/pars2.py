#Скрипт выводит на печать url последней страницы поиска авито


import csv
import requests
u_rl = 'https://www.avito.ru/moskva/telefony?p=1&q=htc'
from bs4 import BeautifulSoup
# Запрос к веб странице
def get_html(url):
    response = r = requests.get(url)
    return response.text

def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    #Класс = значению из html кода (следующая страница)
    pages = soup.find('div', class_='pagination-pages')

def main():
    rtext = (get_html(u_rl))
    soup = BeautifulSoup(rtext, 'lxml')
    pages = soup.find('div', class_='pagination-pages')
    print(pages)

if __name__ == '__main__':
    main()