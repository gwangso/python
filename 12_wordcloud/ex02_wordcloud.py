from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/results?search_query=키보드")
time.sleep(2)