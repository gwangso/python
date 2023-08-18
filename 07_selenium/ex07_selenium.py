from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 드라이버 경로설정
driver = webdriver.Chrome()
driver.get("https://comic.naver.com/webtoon")

# 페이지가 로드되고 나야 요소들에 접근이 가능
# 그런데 페이지가 전부 로드되지 않고 페이지가 끝남
# 따라서 접근하고 sleep을 조금 줘야한다.
time.sleep(3) 

# 웹툰재목 크롤링
webtoon_title = driver.find_elements(By.CLASS_NAME, 'ContentTitle__title--e3qXt')

cnt = 0
for title in webtoon_title:
    print(title.text)
print(len(webtoon_title))