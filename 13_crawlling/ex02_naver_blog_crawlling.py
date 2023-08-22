from selenium import webdriver
from selenium.webdriver.common.by import By
from collections import Counter
from konlpy.tag import Okt
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from wordcloud import WordCloud
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

#한글깨짐 방지
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

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
driver.get("https://search.naver.com/search.naver?where=blog&sm=tab_viw.blog&query=intp&nso=")
time.sleep(1)

scroll_func()
WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[class="api_txt_lines total_tit"]')))

data = driver.find_elements(By.CSS_SELECTOR, '[class="api_txt_lines total_tit"]')

title_list = []
url_list = []

for dd in data:
    title_list.append(dd.text)
    url_list.append(dd.get_attribute("href"))

# # 블로그에서 태그를 가져와 할 예정이였으나
# # 태그를 어떤 경로로 찾아봐도 가져오지 못해서 
# # 포기
# tags_list = []
# for url in url_list:
#     driver.get(url)
    
#     time.sleep(2)
    
#     tags = driver.find_elements(By.CSS_SELECTOR, 'div#post_footer_contents div div a span.ell')
#     # print(tags)
#     # data_tags = []
#     for tag in tags:
#         print(tag.text,".")
#         # tag_text = tag.text.replace("#","")
#         # tag_vo.append(tag_text)

okt = Okt()

key_list = []
word_list = []
for title in title_list:
    key = []
    for word,tag in okt.pos(title):
        if tag in ["Noun", "Adjective"]:
            key.append(word)
            word_list.append(word)
    key_list.append(key)

title_list_count = Counter(word_list)

masking_image = np.array(Image.open('cloud.png'))

wc = WordCloud(
    font_path='NanumGothic.ttf',
    width=1200,
    height=1000,
    background_color='white',
    mask=masking_image
)

result = wc.generate_from_frequencies(title_list_count)

plt.axis('off')
plt.imshow(result)
plt.show()


info = pd.DataFrame(
    {
        "title" : title_list,
        "url" : url_list,
        "keyword" : key_list
    }
)

info.to_csv("./INTP.csv", encoding='UTF-8-sig')