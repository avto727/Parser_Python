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
    with open('j50.csv', 'a') as f:
        writer = csv.writer(f, delimiter=';', lineterminator='\n')
        writer.writerow( (date['profecy'], date['firm'], date['price'], date['url']) )

# функция сбора данных со страницы поиска
def get_page_data(html):
    # выборка нужных данных
    soup = BeautifulSoup(html, 'lxml')
    # print(soup)     #выбираем всю таблицу
    ads = soup.find('td', id='resultsCol')# id='resultsCol')#, class_='search-table'
    # ads = kds.find_all('table', class_='search-table')   find_all('td').
    print(ads)
    # for ad in ads:
    # #     #profecy, firm, price, date, url
    #     try:
    #         profecy = ad.find('a', class_='profecy').text.strip()
    #     except:
    #         profecy = ''
    #     try:
    #         firm = ad.find('a', class_='search-param-firm').text.strip()
    #     except:
    #         firm = ''
    #     try:
    #         url = ad.find('a', class_='profecy').get('href')
    #     except:
    #         url = ''
    #     try:
    #         price = ad.find('span', class_='search-earning').text.strip()
    #     except:
    #         price = ''
    #     # try:
    #     #     date = ad.find('td', class_='valign').find_all('align').text.strip()
    #     # except:
    #     #     date = ''
    #     data = {'profecy':profecy,
    #             'firm':firm,
    #             'price':price,
    #             'url':url}
    #     write_csv(data)

def main():
    url = 'https://ru.indeed.com/jobs?q=%D0%A2%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5&start=170'
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
        html = get_html(url)
        # print(html)
        get_page_data(html)

if __name__ == '__main__':
    main()
