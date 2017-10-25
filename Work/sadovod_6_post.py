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
import json
import urllib.parse


def init_driver():
    driver = webdriver.PhantomJS()
    # driver.wait = WebDriverWait(driver, 1)
    return driver


def lookup(driver, num):
    driver.get("https://sadovod.city/category/66")
    try:
            button = driver.find_element_by_link_text(num)
            button.click()
    except TimeoutException:
        print("Box or Button not found in sadovod.city")


if __name__ == "__main__":
    driver = init_driver()
    num = '3'
    lookup(driver, num)
    time.sleep(5)
    num = '5'
    lookup(driver, num)
    time.sleep(3)
    driver.quit()