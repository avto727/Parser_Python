# Скрипт распарсивает список участников из формата json в список
# и записывает список в csv файл в один столбец


import requests
import json
import csv
r=requests.get('https://api.vk.com/method/groups.getMembers',params={'group_id':71452958,'sort':'id_asc'})
# print(r)
resp = r.json()
jstr = resp['response']
print (jstr)
jstrl = jstr['count']#   количество участников группы
print (jstrl)
z = jstr['users']
print (z)
with open('list_to_csv.csv', 'a', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    for item in z:
        csv_writer.writerow([item])
        