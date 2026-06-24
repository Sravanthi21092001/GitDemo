import time
from selenium import webdriver
driver = webdriver.Chrome()


driver.get("https://rahulshettyacademy.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.quit()
time.sleep(2)




















