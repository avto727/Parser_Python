import requests
from bs4 import BeautifulSoup

base_url = 'https://ru.indeed.com/jobs?q=%D0%A2%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5&start=170'
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
    table = soup.find('table', role='main')
    rows = soup.find_all('div', class_='row  result')
    print(table)
    projects = []
    for row in rows:
        profecy = row.find('a')
        catcols = row.find('a', class_='search-param-firm')
        prcols = row.find('a', class_='profecy')
        apcols = row.find('span', class_='search-earning')
        print(profesy)
        projects.append({
            'title': profecy[2].text,
            'categories': catcols.text.strip(),
            'price': prcols.text.strip(),
            'application': apcols.text.strip()
        })
    for project in projects:
        print(project)

def main():
    i = 0
    # page_count = get_page_count(get_html(base_url))
    # print('Всего найдено страниц ', page_count )
    projects = []
    for page in range(0, 1):# Ограничим диапазон поиска, вместо page_count поставим 3
        i += 1
        url_gen = base_url# + '&page=' + str(page)
        par = parse(get_html(url_gen))
        projects.append(par)
        for project in projects:
            pass

if __name__ == '__main__':
    main()