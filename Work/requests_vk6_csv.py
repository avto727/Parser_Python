# Скрипт распарсивает список участников из формата json в список
# и ДОПИСЫВАЕТ список в csv файл в одну строку


import requests
import json
import csv

r = requests.get('https://api.vk.com/method/groups.getMembers', params={'group_id': 71452958, 'sort': 'id_asc'})
# print(r)
resp = r.json()
jstr = resp['response']
print (jstr)
jstrl = jstr['count']  # количество участников группы
print (jstrl)
z = jstr['users']
with open('z.csv', 'a') as f:
    writer = csv.writer(f, delimiter=';', lineterminator='\n')
    writer.writerow(z)
print (z)

