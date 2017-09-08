def main():
    url = 'https://hh.ru/search/vacancy?clusters=true&text=Программист&enable_snippets=true&search_field=name&area=1&page=0'
    #Начало url
    base_url = 'https://hh.ru/search/vacancy?clusters=true&text='
    #СЛОВО ПОИСКА
    vacan = 'Программист'
    # Поисковый запрос
    query_part = '&enable_snippets=true&search_field=name&area=1&page='
    total_pages = get_total_pages(get_html(url))
    for i in range(0, 3):#задаем диапазон просматриваемых страниц. вместо total_pages  ставим 3
        #   Формирование url (склеивание)
        url_gen = base_url + vacan + query_part + str(i)
        print(url_gen)
        # html = get_html(url_gen)
        # get_page_data(html)

if __name__ == '__main__':
    main()