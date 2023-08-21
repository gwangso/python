from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/feed/trending")

time.sleep(2)

titles = driver.find_elements(By.XPATH, '//*[@id="video-title-link"]')

# 제목 저장을 위한 리스트
title_list = []
# 조회수 저장을 위한 리스트
hits_list = []

for title in titles:
    if title.get_attribute("aria-label"):
        # aria-label 속성값 가져오기
        aria_label = title.get_attribute("aria-label")
        start_index = aria_label.rfind("조회수")+4
        end_index = aria_label.rfind("회")
        hits = aria_label[start_index:end_index]
        hits = int(hits.replace(",",""))

        # print("제목 :", title.get_attribute("title"))
        # print("조회수 :", hits)

        # 제목, 조회수를 각각 리스트에 담기
        # append(): 리스트에 데이터 추가 할 때 사용하는 함수
        title_list.append(title.text)
        hits_list.append(hits)

# print("제목 리스트", title_list)
# print("조회수 리스트", hits_list)

# 제목, 조회수 리스트 함께 조회
for title, hit in zip(title_list, hits_list):
    print(title, hit)