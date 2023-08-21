from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# 무한스크롤 함수
def scroll_fun():
    run = True
    while run:
        before_height = driver.execute_script("return document.documentElement.scrollHeight")    

        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")
        time.sleep(1)

        after_height = driver.execute_script("return document.documentElement.scrollHeight")   
        
        if before_height == after_height:
            run=False
        elif int(after_height) >= 50000:
            run=False    

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/results?search_query=키보드")
time.sleep(2)

# 무한 스크롤 함수
scroll_fun()

titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')

# 제목 저장을 위한 리스트
title_list = []
# 조회수 저장을 위한 리스트
hits_list = []

for title in titles:

    if title.get_attribute("aria-label") and title.text and "YouTube 영화" not in title.get_attribute("aria-label"):
        # aria-label 속성값 가져오기
        aria_label = title.get_attribute("aria-label")
        start_index = aria_label.rfind("조회수")+4
        end_index = aria_label.rfind("회")
        hits = aria_label[start_index:end_index]
        # 조회수가 1000 이상인 영상
        if "," in hits:
            hits = int(hits.replace(",",""))
        # 조회수가 1,000이하 영상
        elif not hits:
            hits = 0 
        else :
            hits = int(hits)
        
        # 동일한 제목 영상은 한 번만
        if title.text not in title_list:
            # 제목, 조회수를 각각 리스트에 담기
            # append(): 리스트에 데이터 추가 할 때 사용하는 함수
            title_list.append(title.text)
            hits_list.append(hits)

crawling_result = {
    "title" : title_list,
    "hits" : hits_list
}

result = pd.DataFrame(crawling_result)
# dataFrame을 csv로 저장
# result.to_csv("./result.csv", encoding="utf-8-sig")
# 조회수 내림차순으로 정렬 후 csv로 저장
result.sort_values(by=["hits"], ascending=False).to_csv("./result.csv", encoding="utf-8-sig")
