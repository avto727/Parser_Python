import requests
from bs4 import BeautifulSoup

base_url = 'https://www.superjob.ru'
def get_html(url):
    r = requests.get(url)
    # print(r.text)
    return r.text

def get_page_count(html):
    soup = BeautifulSoup(html, 'lxml')
    pagination = soup.find('ul', class_='pagination')
    page_count = pages = pagination.find_all('a')[-1].get('href').split('=')[2]
    return int(page_count)

def parse(html):
    soup = BeautifulSoup(html, 'lxml')
    print(soup)
    # button_4 = driver.find_element_by_xpath('.//a[@MainPageSearch_tab h_color_blue h_border_dotted"][contains(., "Поиск сотрудников")]')
    # button_4.click()
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
    url = 'https://www.superjob.ru/resume/search_resume.html'
    i = 0
    # page_count = get_page_count(get_html(base_url))
    # print('Всего найдено страниц ', page_count )
    projects = []
    for page in range(0, 1):# Ограничим диапазон поиска, вместо page_count поставим 3
        i += 1
        url_gen = url# + '&page=' + str(page)
        par = parse(get_html(url_gen))
        projects.append(par)
        for project in projects:
            pass

if __name__ == '__main__':
    main()