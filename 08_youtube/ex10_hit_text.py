from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")

time.sleep(2)

titles = driver.find_elements(By.XPATH, '//*[@id="video-title-link"]')



for title in titles:
    if title.get_attribute("aria-label"):
        # aria-label 속성값 가져오기
        aria_label = title.get_attribute("aria-label")
        start_index = aria_label.rfind("조회수")+4
        end_index = aria_label.rfind("회")
        hits = aria_label[start_index:end_index]
        hits = int(hits.replace(",",""))
        print("제목 :", title.get_attribute("title"))
        print("조회수 :", hits)

        