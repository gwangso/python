from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 드라이버 경로설정
driver = webdriver.Chrome()
driver.get("https://comic.naver.com/webtoon")

# 웹툰재목 크롤링
webtoon_title = driver.find_elements(By.CLASS_NAME, 'ContentTitle__title--e3qXt')

for title in webtoon_title:
    print(title.text)

time.sleep(3)