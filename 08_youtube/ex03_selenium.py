from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys #키보드의 키를제어하는 명령어
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

query = input("검색 > ")
query = query.replace(" ", "+")

url = "https://www.youtube.com/results?search_query="+query

driver = webdriver.Chrome()
driver.get(url)

element = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="video-title"]/yt-formatted-string')))

titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]/yt-formatted-string')

for title in titles:
    print(title.text)