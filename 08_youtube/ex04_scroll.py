from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys #키보드의 키를제어하는 명령어
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")

# javascript로 현제 페이지 높이값 가져오기
# execute_script(): javascript 코드를 실행해주는 함수
# javascript 실행값으 파이썬 변수로 받으려면 return을 작성해야 함

# h1: 처음페이지 열었을 때 높이 값

h1 = driver.execute_script("return document.documentElement.scrollHeight")
print("처음높이 : ", h1)

driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight)")
time.sleep(1)

h2 = driver.execute_script("return document.documentElement.scrollHeight")
print("두번째 높이: ", h2)

driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight)")
time.sleep(1)

h3 = driver.execute_script("return document.documentElement.scrollHeight")
print("세번째 높이: ", h3)