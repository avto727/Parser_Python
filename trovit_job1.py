import requests
from bs4 import BeautifulSoup
import csv

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
    with open('yan_job.csv', 'a') as f:
        writer = csv.writer(f, delimiter=';', lineterminator='\n')
        writer.writerow( (date['title'], date['price'], date['metro'], date['url']) )

# функция сбора данных со страницы поиска
def get_page_data(html):
    # выборка нужных данных
    soup = BeautifulSoup(html, 'lxml')
    # print(soup)
    kds = soup.find('div', class_='wrapper_search_column')
    # ads = kds.find_all('div', class_='item-info')
    print(kds)
    # for ad in ads:
    #     #title, price, metro, url
    #     try:
    #         title = ad.find('div', class_='description').find('h3').text.strip()
    #     except:
    #         title = ''
    #     try:
    #         url = 'https://www.avito.ru' + ad.find('div', class_='description').find('h3').find('a').get('href')
    #     except:
    #         url = ''
    #     try:
    #         price = ad.find('div', class_='about').text.strip()
    #     except:
    #         price = ''
    #     try:
    #         metro = ad.find('div', class_='data').find_all('p')[-1].text.strip()
    #     except:
    #         metro = ''
    #
    #     data = {'title':title,
    #             'price':price,
    #             'metro':metro,
    #             'url':url}
    #
    #     write_csv(data)

def main():
    url = 'https://ru.trovit.com/rabota/index.php/cod.search_jobs/type.0/what_d.python/where_d.moscow/sug.0/isUserSearch.1/origin.1'
    #Начало url
    base_url = 'https://ru.trovit.com/rabota/index.php/cod.search_jobs/type.0/what_d.'
    #СЛОВО ПОИСКА
    vacan = 'pytho'
    # Поисковый запрос
    query_part = '/where_d.'
    where = 'moscow'
    query_part_2 = '/sug.0/isUserSearch.1/origin.1'
    # total_pages = get_total_pages(get_html(url))
    for i in range(0, 1):#задаем диапазон просматриваемых страниц. вместо total_pages  ставим 3
        #   Формирование url (склеивание)
        url_gen = base_url + vacan + query_part + where + query_part_2
        html = get_html(url_gen)
        # print(html)
        get_page_data(html)

if __name__ == '__main__':
    main()