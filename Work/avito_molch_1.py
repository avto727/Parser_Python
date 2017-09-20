#   Скрипт выясняет количество страниц поиска на авито и формирует список урлов на страницы выдачи
#
#


import requests
from bs4 import BeautifulSoup


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
    # Разбиваем строку на символы  по знаку =, выбираем второй элемент [1]  иеще раз делим по & и берем первый
    # элемент [0]
    total_pages = pages.split('=')[1].split('&')[0]
    return int(total_pages)
def main():
    url = 'https://www.avito.ru/moskva/telefony?p=1&q=htc'
    #Начало url
    base_url = 'https://www.avito.ru/moskva/telefony'
    #Номер страницы
    page_part = 'p='
    # Поисковый запрос
    query_part = '&q=htc'
    total_pages = get_total_pages(get_html(url))
    for i in range(1, total_pages):
        #   Формирование url (склеивание)
		url_gen = base_url + page_part + str(i) + query_part
        print(url_gen)

if __name__ == '__main__':
    main()