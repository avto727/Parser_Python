# Скрипт распарсивает список участников из формата json в список
# и записывает список в файл


import requests
import json
r=requests.get('https://api.vk.com/method/groups.getMembers',params={'group_id':71452958,'sort':'id_asc'})
# print(r)
resp = r.json()
jstr = resp['response']
print (jstr)
jstrl = jstr['count']#   количество участников группы
print (jstrl)
z = jstr['users']
print (z)
# for j in range(0, jstrl):#
#     print (j, z[j])
result = open('result.txt','w', encoding='utf8')
json.dump(z,result,ensure_ascii=False)
result.close()
