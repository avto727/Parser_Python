#     Скрипт парсинга сайта weblance.net 
#     выдает результат по видео уроку Пишем парсер web-caйта [Python_Практика]
#     переделан на вывод данных в csv  файл wln.csv (работал, но стал выдавать ошибку)
import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):
    r = requests.get(url)
    return r.text

def write_csv(date):
    with open('wln.csv', 'a', encoding='cp1251') as f:
        writer = csv.writer(f, delimiter=';', lineterminator='\n')
        try:
            writer.writerow( (date['title'], date['categories'], date['price'], date['application']) )
        except:
            pass

def parse(html):
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find('div', class_='container-fluid cols_table show_visited')
    rows = table

    projects = []

    for row in rows:
        try:
            catcols = row.find_all('div', class_='col-sm-1 amount title')
        except:
            catcols = ''
        try:
            apcols = row.find_all('div', class_='col-sm-3 text-right text-nowrap hidden-xs')
        except:
            apcols = ''
        try:
            cols = row.find_all('a')
        except:
            cols = ''
        projects.append({
            'title': cols[0].text,
            'categories': cols[1].text,
            'price': catcols[0].text.strip(),
            'application': apcols[0].text.strip()
        })
    for project in projects:
        write_csv(project)
        print(project)

def main():
    for i in range(1,18):
        print(i)
        url_gen = 'https://www.weblancer.net/jobs/?type=project' + '&page=' + str(i)
        pro = parse(get_html(url_gen))


if __name__ == '__main__':
    main()