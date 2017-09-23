# Скрипт записывает в файл result.txt' id подписчиков группы (в формате json)


import requests
import json
r=requests.get('https://api.vk.com/method/groups.getMembers',params={'group_id':71452958,'sort':'id_asc'}).json()
# print(r)
result = open('result.txt','w', encoding='utf8')
json.dump(r,result,ensure_ascii=False)
result.close()