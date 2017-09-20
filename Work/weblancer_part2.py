#     Скрипт выдает результаты по парсингу сайта на время 10:06 по уроку на видео
# 
# 
import requests
from bs4 import BeautifulSoup

def get_html(url):
    r = requests.get(url)
    return r.text

def parse(html):
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find('div', class_='container-fluid cols_table show_visited')
    rows = table.find_all('h2', class_='title')
    projects = []
    for row in rows:
        cols = row.find_all('a')
        #print(cols)
        projects.append({
            'title': cols[0].text
        })
    for project in projects:
        print(project)

def main():
    #url = 'https://www.weblancer.net/jobs' #https://www.weblancer.net/jobs/?type=project&page=2
    parse(get_html('https://www.weblancer.net/jobs/?type=project'))

if __name__ == '__main__':
    main()