# Скрипт распарсивает список участников группы вк(возможно пойдут) из формата json в список
# проверяет город (1 = Москв
# и записывает список в csv файл в один столбец
#Если кол. участников больше 1000, скрипт автоматом делает несколько запросов по 1000 участников.
#и дописывает в тот же столбец.
#Пишет и друзей и не друзей (Авторизации нет) Фильтр только по городу


import requests
import json
import csv

def get_html(group_id, offset):
    r=requests.get('https://api.vk.com/method/groups.getMembers',params={'group_id':group_id,'filter':'unsure', 'sort':'id_asc','fields':'city','count':1000, 'offset':offset})
# print(r)
    return r.json()

def parser(p_group_id, p_offset):
    resp = get_html(p_group_id, p_offset)
    jstr = resp['response']
    count = jstr['count']  # количество участников группы
    print (count)
    jcount = int(count / 1000) + 1
    print (int(jcount))
    z = jstr['users']
    print (' это z', z)
    with open('list_to_csv.csv', 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        # for jcou in range(0, jcount)
        for j in range(0, 1000):  #
            us = z[j]
            # print (j)
            try:
                c = us['city']
            except:
                c = 2
            id = us['uid']
            fam = us['last_name']
            if c == 1:
                print (j, id, fam, 'city', c)
                csv_writer.writerow([id])
    return jcount

def main():
    m_group_id = 97411113 #Задаем id группы
    m_offset = 0
    jcount = parser(m_group_id, m_offset)
    for k in range(1, jcount):
        m_offset = m_offset + 1000
        print (k)
        parser(m_group_id, m_offset)




if __name__ == '__main__':
    main()
