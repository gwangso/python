# 1. 유튜브 홈페이지 접속
# 2. 검색어 입력
# 3. 검색
# 4. 필터클릭
# 5. 조회수 클릭

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")

search_input = driver.find_element(By.CSS_SELECTOR, 'input#search')
#검색어 입력
search_input.send_keys("tetris 99")
# 엔터치기
search_input.send_keys(Keys.RETURN)
driver.implicitly_wait(time_to_wait=5)

# 필터버튼 요소 점근
filter_button = driver.find_element(By.XPATH, '//*[@id="filter-button"]')
filter_button.click()

#조회수 xPath
#    //*[@id="endpoint"]
#업로드 날짜 xPath
#   //*[@id="endpoint"]

# 조회수 full xPath(절대경로)
#   /html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-search-filter-options-dialog-renderer/div[2]/ytd-search-filter-group-renderer[5]/ytd-search-filter-renderer[3]/a

filter_view = driver.find_element(By.XPATH, '/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-search-filter-options-dialog-renderer/div[2]/ytd-search-filter-group-renderer[5]/ytd-search-filter-renderer[3]/a')
filter_view.click()

from ex06_scroll import scroll_fun

scroll_fun(driver)
time.sleep(2)

titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]/yt-formatted-string')
for title in titles:
    print(title.text)

