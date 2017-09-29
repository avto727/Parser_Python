import requests
from bs4 import BeautifulSoup
import urllib.request
import csv

#Цель - ищу заказы на одной странице

def get_html(url):
    r = requests.get(url)
    return r.text

def write_csv(data):
    with open('sadovod.csv', 'a') as f:
        writer = csv.writer(f, delimiter=';')#, lineterminator='\n'
        writer.writerow( (data['number'], data['article'], data['title'], data['price'], data['sizes'], data['color'], data['facture'], data['date'], data['url']) )


def parse(html):
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find('div', class_='product-list clearfix')
    items = table.find_all('div', class_='product-item')
    i = 1
    for item in items:
        number = i
        try:
            title = item.find('div', class_='description-container text-center').find('a').text.strip()
        except:
            title = ''
        try:
            url = 'https://sadovod.city' + item.find('div', class_='image-container').find('a').get('href')
        except:
            url = ''
        try:
            article = url.split('/')[4]
        except:
            url = ''
        try:
            price = item.find('div', class_='price-container text-right').text.strip()
        except:
            price = ''
        r_2 = requests.get(url).text
        soup = BeautifulSoup(r_2, 'lxml')
        table_2 = soup.find('div', class_='combinations')
        try:
            sizes = table_2.find('div', class_='select col-md-6 col-sm-9').find('select').text.strip()
        except:
            sizes = ''
        try:
            color = table_2.find('div', class_='product-colors form-group').find('select').text.strip()
        except:
            color = ''
        try:
            facture = table_2.find('div', class_='product-tkan form-group').find('p').text.strip()
        except:
            facture = ''
        try:
            pdate = table_2.find('div', class_='product-price form-group').text.strip()
            date = pdate.split(':')[2].split(' ')[1]
        except:
            date = ''
        data = {'number':number,
                'article':article,
                'title':title,
                'price':price,
                'sizes':sizes,
                'color':color,
                'facture':facture,
                'date':date,
                'url':url}
        write_csv(data)
        i += 1


def main():
    #url = 'https://www.weblancer.net/jobs' #https://www.weblancer.net/jobs/?type=project&page=2
    parse(get_html('https://sadovod.city/category/66'))

if __name__ == '__main__':
    main()