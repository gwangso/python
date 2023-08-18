# 조회수값 추출하기

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


aria_label = "16 Y/O UNDERDOG vs. 7-TIME CHAMP 조회수 - Classic Tetris World Championship 2018 Final Round 게시자: Classic Tetris 4년 전 42분 조회수 18,934,958회"

# find(): 해당 변수의 시작지점 부터 찾음
# rfind(): 매개변수로 전달한 글자의 인덱스 값을 반환(해당 변수의 제일 마지막에서 시작하여 찾음)
print(aria_label.find("조회수")) #이럴 경우 제목에 조회수라는 단어가 들어가 있으면 그곳의 인덱스값을 찾아준다.
print(aria_label.rfind("조회수")+4)
print(aria_label.rfind("회"))
print(int(aria_label[123:133].replace(",", "")))
start_index = aria_label.rfind("조회수")+4
end_index = aria_label.rfind("회")
hits = aria_label[start_index:end_index]

print(hits)
print(type(hits))
# 쉼표 제고 후 정수형으로 변환
# replace(): 바꾸기 기능
hits = int(hits.replace(",",""))
print(hits)
print(type(hits))
