from selenium import webdriver

driver = webdriver.Chrome() # or add to your PATH
driver.set_window_size(1024, 768) # optional
driver.get('https://google.com/')
driver.save_screenshot('screen.png') # save a screenshot to disk
sbtn = driver.find_element_by_tag_name("body").get_attribute("inner‌​HTML")
# sbtn = driver.find_element_by_name('button.btnI')
sbtn.click()