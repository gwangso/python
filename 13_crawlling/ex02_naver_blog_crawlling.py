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
driver.get("https://search.naver.com/search.naver?sm=tab_hty.top&where=view&query=intp&oquery=mbti&tqi=iMdm6wprvTossg4K5osssssstnw-452156&mode=normal")
time.sleep(1)

scroll_func()
element = WebDriverWait(driver, 3)
element.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[class="api_txt_lines total_tit _cross_trigger"]')))

data = driver.find_elements(By.CSS_SELECTOR, '[class="api_txt_lines total_tit _cross_trigger"]')

