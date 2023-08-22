from selenium import webdriver
from selenium.webdriver.common.by import By
from konlpy.tag import Okt
from collections import Counter
import time
import numpy as np
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

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
driver.get("https://www.youtube.com/feed/trending")
time.sleep(1)

scroll_func()
time.sleep(2)

crawlling_data = driver.find_elements(By.XPATH, '//*[@id="video-title"]')

title_list = []
hits_list = []
for data in crawlling_data:
    #쇼츠제외, 더보기 제외, 영화 제외
    if data.get_attribute("aria-label") and data.text and "YouTube 영화" not in data.get_attribute("aria-label"):
        aria_label = data.get_attribute("aria-label")
        start_hits = aria_label.rfind("조회수")+4
        stop_hits = aria_label.rfind("회")
        hits = aria_label[start_hits:stop_hits]
        if not hits:
            hits=0
        elif ',' in hits:
            hits = int(hits.replace(',',''))
        elif ',' not in hits:
            hits = int(hits)
        if data.text not in title_list:
            title_list.append(data.text)
            hits_list.append(hits)

okt = Okt()

word_list = []
for title in title_list:
    for word, tag in okt.pos(title):
        if tag in ["Noun", 'Adjective']:
            word_list.append(word)

word_list_count = Counter(word_list)

masking_image = np.array(Image.open("twiter.png"))

wc = WordCloud(
    font_path='./NanumGothic.ttf',
    width=1500,
    height=1200,
    background_color='white',
    mask=masking_image
)

result = wc.generate_from_frequencies(word_list_count)

plt.axis('off')
plt.imshow(result)
plt.show()

data_list = pd.DataFrame(
    {
        "title" : title_list,
        "hits" : hits_list
    }
)

data_list.sort_values(by=["hits"]).to_csv("./result.csv", encoding="UTF-8-sig")