from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys #키보드의 키를제어하는 명령어
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")

# 검색창 요소 접근
search_input = driver.find_element(By.CSS_SELECTOR, 'input#search')
#검색어 입력
search_input.send_keys("tetris 99")
# 엔터치기
search_input.send_keys(Keys.RETURN)

# # 버튼클릭
# search_button = driver.find_element(By.XPATH, '//*[@id="search-icon-legacy"]')
# search_button.click()

element = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="video-title"]/yt-formatted-string')))

titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]/yt-formatted-string')

for title in titles:
    print(title.text) # innerHTML 값
    # print(title.tag_name) # 해당 요소의 태그이름을 가져옴
    # print(title.get_attribute("aria-label")) # 해당 요소의 aria-label 속성값을 가져오기

# https://www.youtube.com/results?search_query=tetris+99
# https://www.youtube.com/results?search_query=테트리스+뿌요뿌요