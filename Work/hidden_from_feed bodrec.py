#Скрипт использует методы friends.get и users.get vk_api
#Авторизация по токену приложения
#    Проверяем кто из друзей читает ленту
#    Скрипт перебирает id  из указанного диапазона
#  Токен для Bodrec@mail.ru

import vk
import time

session = vk.Session(access_token='4486fe808ab...15ff10da1d1')
vkapi = vk.API(session)
friends = vkapi('friends.get')
i = 0 #Здесь и
while i < 150 : #здесь задаем диапазон
    id = friends[i]
    # id = 35917522
#print(friends # - так можно вывести спиоок всех друзей
    users = vkapi('users.get', user_id=id, fields='is_hidden_from_feed')
    print(i, users)
    time.sleep(1)
    i += 1
