# Скрипт выводит id подписчиков группы


import requests
import json
r=requests.get('https://api.vk.com/method/groups.getMembers',params={'group_id':71452958,'sort':'id_asc'})
print(r.json())