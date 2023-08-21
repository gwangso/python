from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")

titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')

for title in titles:
    print(title.text) # innerHTML 값
    print(title.tag_name) # 해당 요소의 태그이름을 가져옴
    print(title.get_attribute("aria-label")) # 해당 요소의 aria-label 속성값을 가져오기