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
url = 'https://wikium.ru/'
driver.get(url)
text_1 = 'Начать развиваться'
# print(driver.page_source)
try:
    button_1 = driver.find_element_by_xpath('.//a[@class="btn  btn--blue"][contains(., "Начать развиваться")]')
    button_1.click()
except TimeoutException:
    print("Box or Button not found in sadovod.city")
button_logo = driver.find_element_by_xpath('.//div[@class="logo"]')
button_logo.click()
button_2 = driver.find_element_by_xpath('.//a[@class="btn btn--blue"][contains(., "НАЧАТЬ РАЗВИВАТЬСЯ")]')
button_2.click()
button_logo = driver.find_element_by_xpath('.//div[@class="logo"]')
button_logo.click()
button_3 = driver.find_element_by_xpath('.//a[@class="btn btn--blue"][contains(., "НАЧАТЬ ТРЕНИРОВАТЬСЯ")]')
button_3.click()
button_logo = driver.find_element_by_xpath('.//div[@class="logo"]')
button_logo.click()
button_4 = driver.find_element_by_xpath('.//a[@class="btn btn--blue"][contains(., "НАЧАТЬ ТРЕНИРОВКУ")]')
button_4.click()
button_logo = driver.find_element_by_xpath('.//div[@class="logo"]')
button_logo.click()
button_5 = driver.find_element_by_xpath('.//a[@class="landing-reviews__btn  btn  btn--blue"][contains(., "ПРИСОЕДИНИТЬСЯ К ВИКИУМ")]')
button_5.click()
button_logo = driver.find_element_by_xpath('.//div[@class="logo"]')
button_logo.click()
button_6 = driver.find_element_by_xpath('.//a[@class="landing-footer__btn  btn  btn--blue"][contains(., "НАЧАТЬ РАЗВИВАТЬСЯ")]')
button_6.click()
button_logo = driver.find_element_by_xpath('.//div[@class="logo"]')
button_logo.click()
driver.quit()
# button_7 = driver.find_element_by_xpath('.//a[@class="landing-footer__links"][contains(., "Помощь")]')
# button_7.click()
