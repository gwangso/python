from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 무한스크롤 함수
def scroll_fun(driver):
    run = True
    while run:
        before_height = driver.execute_script("return document.documentElement.scrollHeight")    
        print(before_height)

        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")
        time.sleep(1)

        after_height = driver.execute_script("return document.documentElement.scrollHeight")   
        print(after_height)
        
        if before_height == after_height:
            run=False
        elif int(after_height) >= 50000:
            run=False