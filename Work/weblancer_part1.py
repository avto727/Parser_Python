#Скрипт парсит сайт weblance.net
# Задаем url/ Первый проход - выделяем таблицу(table). Второй проход - выделяем строки(rows)/Третий проход -
# выделяем столбцы (cols)
import requests
from bs4 import BeautifulSoup
import urllib.request

#Цель - ищу заказы на одной странице

def get_html(url):
    r = requests.get(url)
    return r.text

def parse(html):
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find('div', class_='container-fluid cols_table show_visited')
    rows = table.find_all('h2', class_='title')

    for row in rows:
        cols = row.find_all('a')
        print(cols)

def main():
    #url = 'https://www.weblancer.net/jobs' #https://www.weblancer.net/jobs/?type=project&page=2
    parse(get_html('https://www.weblancer.net/jobs/?type=project'))

if __name__ == '__main__':
    main()