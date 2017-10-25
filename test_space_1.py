import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException
import requests
from bs4 import BeautifulSoup
import urllib.request
import csv


driver = webdriver.Chrome()
url = 'http://sapr.space1s.ru'
fam = 'Иванов'
driver.get(url)
time.sleep(3)
query = 'avto727@bk.ru'
#   Выбрать из списка
button_1 = driver.find_element_by_id('userList')
button_1.click()
# клик "Вход без пароля"
button_2 = driver.find_element_by_xpath('.//ol[@class="editDropDownList editDropDownListOldNeo"][contains(., "Вход (без пароля)")]')
button_2.click()
#  Клик Ок
button_3 = driver.find_element_by_id('okButton')
button_3.click()
time.sleep(5)
#  Клик Кнопки Далее
button_4 = driver.find_element_by_id('form0_ФормаДалее')
button_4.click()
time.sleep(3)
#  Выбор окна ввода фамилии
box_1 = driver.find_element_by_id('form0_Фамилия_div')
box_1.click()
#  Отправка фамилии в окно
box_1.send_keys('Иванов')

# print(driver.page_source)
# button_11 = driver.find_element_by_xpath('.//button[@class="landing-reviews__btn-more  link  link--underline"]')
# button_11.click()


# button_12 = driver.find_element_by_id('lang-select')
# button_12.click()
# button_14 = driver.find_element_by_xpath('.//label[@class="custom-select__item-label"][contains(., "Русский")]')
# button_14.click()
# button_logo = driver.find_element_by_xpath('.//div[@class="logo"]')
# button_logo.click()
# button_2 = driver.find_element_by_xpath('.//a[@class="btn btn--blue"][contains(., "НАЧАТЬ РАЗВИВАТЬСЯ")]')
# button_2.click()
# button_logo = driver.find_element_by_xpath('.//div[@class="logo"]')
# button_logo.click()
# button_3 = driver.find_element_by_xpath('.//a[@class="btn btn--blue"][contains(., "НАЧАТЬ ТРЕНИРОВАТЬСЯ")]')
# button_3.click()
# button_logo = driver.find_element_by_xpath('.//div[@class="logo"]')
# button_logo.click()
# button_4 = driver.find_element_by_xpath('.//a[@class="btn btn--blue"][contains(., "НАЧАТЬ ТРЕНИРОВКУ")]')
# button_4.click()
# button_logo = driver.find_element_by_xpath('.//div[@class="logo"]')
# button_logo.click()
# button_5 = driver.find_element_by_xpath('.//a[@class="landing-reviews__btn  btn  btn--blue"][contains(., "ПРИСОЕДИНИТЬСЯ К ВИКИУМ")]')
# button_5.click()
# button_logo = driver.find_element_by_xpath('.//div[@class="logo"]')
# button_logo.click()
# button_6 = driver.find_element_by_xpath('.//a[@class="landing-footer__btn  btn  btn--blue"][contains(., "НАЧАТЬ РАЗВИВАТЬСЯ")]')
# button_6.click()
# button_logo = driver.find_element_by_xpath('.//div[@class="logo"]')
# button_logo.click()

# button_7 = driver.find_element_by_link_text('У меня уже есть аккаунт')
# button_7.click()
# button_logo = driver.find_element_by_xpath('.//div[@class="logo"]')
# button_logo.click()
# button_8 = driver.find_element_by_link_text('Помощь')
# button_8.click()
# button_9 = driver.find_element_by_link_text('Пресс-служба')
# button_9.click()
# button_10 = driver.find_element_by_xpath('.//button[@class="landing-reviews__btn-more  link  link--underline"]')
# button_10.click()
# driver.quit()

# button_1 = driver.find_element_by_xpath('.//a[@class="btn  btn--blue"][contains(., "Начать развиваться")]')
# button_1.click()
# #   Установка галочки в чекбокс 1
# chek_box_1 = driver.find_element_by_xpath('.//label[@class="skill__label  skill__label--left  skill__label--abstraction"]')
# chek_box_1.click()
# # Клик кнопки "Продолжить"
# button_15 = driver.find_element_by_name('button')
# button_15.click()
# time.sleep(1)
# #   Установка галочки в чекбокс 5
# chek_box_5 = driver.find_element_by_xpath('.//label[@class="skill__label  skill__label--left  skill__label--learning"]')
# chek_box_5.click()
# # Клик кнопки "Продолжить"
# button_16 = driver.find_element_by_id('js-slider-button')
# button_16.click()
# time.sleep(1)
# #   Установка галочки в чекбокс 9
# chek_box_9 = driver.find_element_by_xpath('.//label[@class="skill__label  skill__label--left  skill__label--decision"]')
# chek_box_9.click()
# # Клик кнопки "Продолжить"
# button_17 = driver.find_element_by_id('js-slider-button') # Кнопка Зарегистрироваться
# button_17.click()
# box_1 = driver.find_element_by_name('Form_User_RegisterNoPasswordForm[email]') # Ввод e-mail для регистрации
# box_1.send_keys(query)
# # Кнопка Зарегистрироваться
# button_18 = driver.find_element_by_name('button')
# button_18.click()