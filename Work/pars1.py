#Скрипт выводит на печать html код страницы. весь


import csv
import requests

from bs4 import BeautifulSoup
# Запрос к веб странице
def get_html(url):
    response = r = requests.get(url)
    return response.text

#def parse(html):
#    soup = BeautifulSoup(html)
#    table = soup.find('body', class_='itemsListElement')
#    #print(table.prettify())

def main():
    print(get_html('https://www.avito.ru/moskva/telefony?p=1&q=htc'))


if __name__ == '__main__':
    main()