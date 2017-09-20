#     Скрипт парсинга сайта weblance.net 
#     выдает результат по видео уроку Пишем парсер web-caйта [Python_Практика]
#     на момент 13 : 56 
import requests
from bs4 import BeautifulSoup

def get_html(url):
    r = requests.get(url)
    return r.text

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
    #url = 'https://www.weblancer.net/jobs' #https://www.weblancer.net/jobs/?type=project&page=2
    parse(get_html('https://www.weblancer.net/jobs/?type=project'))

if __name__ == '__main__':
    main()