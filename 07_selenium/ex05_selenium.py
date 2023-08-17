from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.naver.com/")

# 검색창 접근, 검색어 입력
# 검색버튼 클릭
search_element = driver.find_element(By.XPATH,'//*[@id="query"]')

#검색어 입력
search_element.send_keys("오늘날씨")

#검색버튼 클릭
search_button = driver.find_element(By.XPATH, '//*[@id="sform"]/fieldset/button')
search_button.click()

time.sleep(10)