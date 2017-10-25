import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support.ui import Select
import requests
from bs4 import BeautifulSoup
import urllib.request
import csv


driver = webdriver.Chrome()
url = 'https://www.superjob.ru/resume/search_resume.html'
driver.get(url)
query_1 = 'программист 1С'  #Сюда пишем искомое ключевое слово.
query_2 = 'Москва'
query_3 = 'Римская'
query_4 = 'Россия'
box_1 = driver.find_element_by_name('keywords[0][keys]') # Ввод ключевые слова
box_1.send_keys(query_1)

# Нажимаем  выбор 1 (Поиск по)
select_1 = driver.find_element_by_name('keywords[0][skwc]')
select_1.click()
# Кликаем выбранное
select_1_1 = driver.find_element_by_xpath('.//option[@value="and"][contains(., "всем словам")]')
select_1_1.click()
# select_1_2 = driver.find_element_by_xpath('.//option[@value="or"][contains(., "хотя бы одному слову")]')
# select_1_2.click()
# select_1_3 = driver.find_element_by_xpath('.//option[@value="particular"][contains(., "точной фразе")]')
# select_1_3.click()
# select_1_4 = driver.find_element_by_xpath('.//option[@value="nein"][contains(., "словам-исключениям")]')
# select_1_4.click()

# Нажимаем  выбор 2 (расположенным в )
select_2 = driver.find_element_by_name('keywords[0][srws]')
select_2.click()
# Кликаем выбранное
select_2_1 = driver.find_element_by_xpath('.//option[@value="7"][contains(., "тексте резюме")]')
select_2_1.click()
# select_2_2 = driver.find_element_by_xpath('.//option[@value="50"][contains(., "опыте")]')
# select_2_2.click()
# select_2_3 = driver.find_element_by_xpath('.//option[@value="60"][contains(., "желаемой должности")]')
# select_2_3.click()
# select_2_4 = driver.find_element_by_xpath('.//option[@value="8"][contains(., "названии организации")]')
# select_2_4.click()
# select_2_5 = driver.find_element_by_xpath('.//option[@value="3"][contains(., "ключевых навыках")]')
# select_2_5.click()
# select_2_6 = driver.find_element_by_xpath('.//option[@value="6"][contains(., "образовании и курсах")]')
# select_2_6.click()
# select_2_7 = driver.find_element_by_xpath('.//option[@value="2"][contains(., "месте проживания")]')
# select_2_7.click()

# Выбираем дату публикации
# select_3_1 = driver.find_element_by_xpath('.//div[@class="sj_btn m_group m_first"][contains(., "24 часа")]')
# select_3_1.click()
select_3_2 = driver.find_element_by_xpath('.//div[@class="sj_btn m_group"][contains(., "3 дня")]')
select_3_2.click()
# select_3_3 = driver.find_element_by_xpath('.//div[@class="sj_btn m_group"][contains(., "неделю")]')
# select_3_3.click()
# select_3_4 = driver.find_element_by_xpath('.//div[@class="sj_btn m_group"][contains(., "2 недели")]')
# select_3_4.click()
# select_3_5 = driver.find_element_by_xpath('.//div[@class="sj_btn m_group"][contains(., "1 месяц")]')
# select_3_5.click()
# select_3_6 = driver.find_element_by_xpath('.//div[@class="sj_btn m_group m_last"][contains(., "2 месяца")]')
# select_3_6.click()

# выбираем место работы
select_4_1 = driver.find_element_by_xpath('.//div[@class="sj_btn m_group m_first"][contains(., "на территории работодателя")]')
select_4_1.click()
# select_4_2 = driver.find_element_by_xpath('.//div[@class="sj_btn m_group"][contains(., "на дому")]')
# select_4_2.click()
# select_4_3 = driver.find_element_by_xpath('.//div[@class="sj_btn m_group m_last"][contains(., "разъездного характера")]')
# select_4_3.click()
# Укажите город
box_2 = driver.find_element_by_xpath('.//input[@ng-model="model"]')
box_2.send_keys(query_2)
# box_2.click()
# Подтверждаем совпадение
# time.sleep(2)
# box_2_1 = driver.find_element_by_xpath('.//a[@class="sj_input ResumeSearchForm_input_with_ico g_suggest_input ng-isolate-scope ng-valid ui-autocomplete-input ng-dirty"]')
# keyPress("ddObjectType", "\\13")
# selenium.click(dropdown)

# показывать резюме соискателей из других городов, готовых переехать
# checkbox_1 = driver.find_element_by_name('moveable')
# checkbox_1.click()

# Ближайшая станция метро
box_3 = driver.find_element_by_xpath('.//input[@class="sj_input ResumeSearchForm_input_with_ico g_suggest_input ng-isolate-scope ng-pristine ng-valid ui-autocomplete-input"]')
box_3.send_keys(query_3)

# Тип занятости
select_5 = driver.find_element_by_name('type_of_work')
select_5.click()
# Кликаем выбранное
# select_5_1 = driver.find_element_by_xpath('.//option[@value="0"][contains(., "не имеет значения")]')
# select_5_1.click()
select_5_2 = driver.find_element_by_xpath('.//option[@value="6"][contains(., "полный рабочий день")]')
select_5_2.click()
# select_5_3 = driver.find_element_by_xpath('.//option[@value="10"][contains(., "неполный рабочий день")]')
# select_5_3.click()
# select_5_4 = driver.find_element_by_xpath('.//option[@value="12"][contains(., "сменный график работы")]')
# select_5_4.click()
# select_5_5 = driver.find_element_by_xpath('.//option[@value="13"][contains(., "частичная занятость")]')
# select_5_5.click()
# select_5_6 = driver.find_element_by_xpath('.//option[@value="7"][contains(., "временная работа / freelance")]')
# select_5_6.click()
# select_5_7 = driver.find_element_by_xpath('.//option[@value="9"][contains(., "работа вахтовым методом")]')
# select_5_7.click()

# Гражданство

box_4 = driver.find_element_by_name('citizenship[0]')
box_4.send_keys(query_4)

# Образование

select_6 = driver.find_element_by_name('education')
select_6.click()
# Кликаем выбранное
# select_6_1 = driver.find_element_by_xpath('.//option[@value="0"][contains(., "Не имеет значения")]')
# select_6_1.click()
select_6_2 = driver.find_element_by_xpath('.//option[@value="2"][contains(., "Высшее")]')
select_6_2.click()
# select_6_3 = driver.find_element_by_xpath('.//option[@value="3"][contains(., "Неполное высшее")]')
# select_6_3.click()
# select_6_4 = driver.find_element_by_xpath('.//option[@value="4"][contains(., "Среднее специальное")]')
# select_6_4.click()
# select_6_5 = driver.find_element_by_xpath('.//option[@value="5"][contains(., "Среднее")]')
# select_6_5.click()
# select_6_6 = driver.find_element_by_xpath('.//option[@value="6"][contains(., "Учащийся школы")]')
# select_6_6.click()

# с фотографией
checkbox_2 = driver.find_element_by_name('has_photo')
checkbox_2.click()
# Найти
button_1 = driver.find_element_by_xpath('.//input[@class="sj_btn m_blue"]')
button_1.click()
#--------------------------------------------------------------------------------------------------------------------

# Вычисляем количество страниц
r = driver.page_source
soup = BeautifulSoup(r, 'lxml')
a = str(soup.find('div', class_='sj_paginator').find_all('div', class_='sj_paginator_btn'))
p = a.split('page=')[4].split('"')[0]
# print(p)



# for i in range(2, p):
r = driver.page_source
soup = BeautifulSoup(r, 'lxml')
table = soup.find('div', class_='sj_flex_col2').find_all('div', class_='ResumeListElementNew js-resume-item ng-scope')
print(table)
# for table in tables:
    # Должность
title = table.find('div', class_='sj_block m_b_1')
    # Зарплатные ожидания
price = table.find('span', class_='sj_text ResumeListElementNew_bold')
age = soup.find_all('span', class_='sj_text')
print(age)
ag = age[2].text
city = age[3].text
move = age[4].text
lang = age[5].text
stage = age[6].text
print(price, city, lang, move, stage)
link = soup.find('div', class_='sj_block m_b_1').find('a').get('href').split('?')[0]
    # print(link)
data = {'title':title,
            'price':price,
            'age':ag,
            'city': city,
            'move':move,
            'lang': lang,
            'stage': stage,}