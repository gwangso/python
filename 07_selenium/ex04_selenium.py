from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.naver.com/")

# 로그인 버튼 xPath 접근
login_button = driver.find_element(By.XPATH,'//*[@id="account"]/div/a')

# 로그인 버튼 클릭
login_button.click()

time.sleep(10)