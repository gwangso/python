from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 드라이버 경로설정
driver = webdriver.Chrome()
driver.get("https://getbootstrap.kr/docs/5.3/getting-started/introduction/")
driver.maximize_window()

element = WebDriverWait(driver, 3)
element.until(EC.presence_of_element_located((By.CLASS_NAME, "bd-links-link d-inline-block rounded")))

nav_link = driver.find_elements(By.CLASS_NAME, "bd-links-link d-inline-block rounded")
for n in nav_link:
    print(n.text)
