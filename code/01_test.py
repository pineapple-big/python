from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element_by_id("username").send_keys("admin")
driver.find_element_by_id("password").send_keys("123456")

time.sleep(3)
driver.quit()
