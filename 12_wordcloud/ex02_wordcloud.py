from selenium import webdriver
from selenium.webdriver.common.by import By
from konlpy.tag import Okt
from collections import Counter
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import time
import numpy as np
from PIL import Image

# 무한스크롤 함수
def scroll_func():
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
# 검색할 브라우저
driver.get("https://www.youtube.com/results?search_query=INTP+분석")
time.sleep(2)

# 무한 스크롤
scroll_func()
time.sleep(3)

# 데이터 긁어오기
data = driver.find_elements(By.XPATH, '//*[@id="video-title"]')

title_list = []
hits_list = []

for figure in data:
    # 쇼츠 걸러내기, 더보기 걸러내기, 영화 걸러내기
    if figure.get_attribute("aria-label") and figure.text and "YouTube 영화" not in figure.get_attribute("aria-label"):
        aria_label = figure.get_attribute("aria-label")
        start_hit = aria_label.rfind("조회수")+4
        end_hit = aria_label.rfind("회")
        hits = aria_label[start_hit:end_hit]
        if not hits:
            hits=0
        elif "," not in hits:
            hits = int(hits)
        elif "," in hits :
            hits = int(hits.replace(",",""))

        #동일한 영상은 한번만
        if figure.text not in title_list:
            title_list.append(figure.text)
            hits_list.append(hits)

okt = Okt()

word_list = []
for title in title_list:
    for word, tag in okt.pos(title):
        if tag in ['Noun', 'Adjective'] :
            word_list.append(word)

word_list_count = Counter(word_list)

masking_image = np.array(Image.open("cloud.png"))

wc = WordCloud(font_path="./NanumGothic.ttf",
                width=1000,
                height=1000,
                background_color='white',
                mask=masking_image
)

result = wc.generate_from_frequencies(word_list_count)

plt.axis('off')
plt.imshow(result)
plt.tight_layout(pad=0)
plt.show()