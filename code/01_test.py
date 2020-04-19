from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("www.baidu.com")
driver.maximize_window()
driver.implicitly_wait(30)

time.sleep(3)
driver.quit()