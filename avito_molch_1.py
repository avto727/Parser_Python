import requests
from bs4 import BeautifulSoup
import csv
# План
#1. Выяснить количество страниц
#2. Сформировать список урлов на страницы выдачи
#3. собрать данные
#

# Функция вывода html кода всей страницы
def get_html(url):
    r = requests.get(url)
    return r.text
#Выясняем количество страниц
def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    #Класс = значению из html кода (следующая страница)
    pages = soup.find('div', class_='pagination-pages').find_all('a', class_='pagination-page')[-1].get('href')
    # Вытаскиваем номер последней страницы
    # Разбиваем строку на символы  по знаку =, выбираем второй элемент [1]  и еще раз делим по & и берем первый
    # элемент [0]
    total_pages = pages.split('=')[1].split('&')[0]
    return int(total_pages)
#Функция сохранения данных в файл  csv
def write_csv(date):
    with open('avito.csv', 'a') as f:
        writer = csv.writer(f, delimiter=';', lineterminator='\n')
        writer.writerow( (date['title'], date['price'], date['metro'], date['url']) )

# функция сбора данных со страницы поиска
def get_page_data(html):
    # выборка нужных данных
    soup = BeautifulSoup(html, 'lxml')
    #print(soup)
    ads = soup.find('div', class_='catalog-list').find_all('div', class_='item_table')
    #print(ads)
    for ad in ads:
        #title, price, metro, url
        try:
            title = ad.find('div', class_='description').find('h3').text.strip()
        except:
            title = ''
        try:
            url = 'https://www.avito.ru' + ad.find('div', class_='description').find('h3').find('a').get('href')
        except:
            url = ''
        try:
            price = ad.find('div', class_='about').text.strip()
        except:
            price = ''
        try:
            metro = ad.find('div', class_='data').find_all('p')[-1].text.strip()
        except:
            metro = ''

        data = {'title':title,
                'price':price,
                'metro':metro,
                'url':url}

        write_csv(data)

def main():
    url = 'https://www.avito.ru/moskva/telefony?p=1&q=htc'
    #Начало url
    base_url = 'https://www.avito.ru/moskva/telefony?'
    #Номер страницы
    page_part = 'p='
    # Поисковый запрос
    query_part = '&q=htc'
    total_pages = get_total_pages(get_html(url))
    for i in range(1, 3):#задаем диапазон просматриваемых страниц. вместо total_pages  ставим 3
        #   Формирование url (склеивание)
        url_gen = base_url + page_part + str(i) + query_part
        #print(url_gen)
        html = get_html(url_gen)
        get_page_data(html)

if __name__ == '__main__':
    main()