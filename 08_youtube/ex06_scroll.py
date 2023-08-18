# while문을 적용하여 무한스크롤 구현
# while문 내부 동작
# 1. 처음 높이값 확인
# 2. 높이만큼 스크롤 내리기
# 3. 높이값 확인
# 4. 높이가 같다면 break로 while문 중단

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 무한스크롤 함수
def scroll_fun():
    run = True
    while run:
        before_height = driver.execute_script("return document.documentElement.scrollHeight")    
        print(before_height)

        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")
        time.sleep(1)

        after_height = driver.execute_script("return document.documentElement.scrollHeight")   
        print(after_height)
        
        
        if before_height == after_height:
            run=False
    #제목 가져오기
    titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')
    return titles

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")

driver.implicitly_wait(time_to_wait=3)
element = WebDriverWait(driver, 10)


# 무한스크롤 함수 호출
titles = scroll_fun()

for title in titles:
    print(title.text)
