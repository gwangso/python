from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/")

id_element = driver.find_element(By.ID,'main_navbar')
print(id_element.text)