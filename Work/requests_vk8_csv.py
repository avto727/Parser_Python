# Скрипт распарсивает список участников из формата json в список
# проверяет город (1 = Москв
# и записывает список в csv файл в один столбец


import requests
import json
import csv
r=requests.get('https://api.vk.com/method/groups.getMembers',params={'group_id':71452958,'sort':'id_asc','fields':'city'})
# print(r)
resp = r.json()
print (resp)
jstr = resp['response']
jstrl = jstr['count']#   количество участников группы
print (jstrl)
z = jstr['users']
print (' это z', z)
with open('list_to_csv.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    for j in range(0, jstrl):  #
        us = z[j]
        # print ('us = ', us)
        try:
            c = us['city']
        except:
            c = 2
        id = us['uid']
        fam = us['last_name']
        if c == 1:
            print (j, id, fam, 'city', c)
            csv_writer.writerow([id])



