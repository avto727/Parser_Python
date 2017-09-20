#     Скрипт парсинга сайта weblance.net 
#     выдает результат по видео уроку Пишем парсер web-caйта [Python_Практика]
#     парсит все страницы открытых проектов (вчера работал, сегодня выдает ошибку)
import requests
from bs4 import BeautifulSoup

base_url = 'https://www.weblancer.net/jobs/?type=project'
def get_html(url):
    r = requests.get(url)
    return r.text

def get_page_count(html):
    soup = BeautifulSoup(html, 'lxml')
    pagination = soup.find('ul', class_='pagination')
    page_count = pages = pagination.find_all('a')[-1].get('href').split('=')[2]
    return int(page_count)

def parse(html):
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find('div', class_='container-fluid cols_table show_visited')
    rows = table
    projects = []
    for row in rows:
        catcols = row.find_all('div', class_='col-sm-1 amount title')
        apcols = row.find_all('div', class_='col-sm-3 text-right text-nowrap hidden-xs')
        cols = row.find_all('a')
        projects.append({
            'title': cols[0].text,
            'categories': cols[1].text,
            'price': catcols[0].text.strip(),
            'application': apcols[0].text.strip()
        })
    for project in projects:
        print(project)

def main():
    i = 0
    page_count = get_page_count(get_html(base_url))
    print('Всего найдено страниц ', page_count )
    projects = []
    for page in range(1, page_count):# Ограничим диапазон поиска, вместо page_count поставим 3
        i += 1
        print(i, 'Process parsing  ', (page/page_count * 100))
        url_gen = base_url + '&page=' + str(page)
        par = parse(get_html(url_gen))
        projects.append(par)
        for project in projects:
            pass

if __name__ == '__main__':
    main()