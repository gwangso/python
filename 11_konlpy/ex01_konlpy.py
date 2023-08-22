from konlpy.tag import Kkma
from konlpy.tag import Okt
from collections import Counter 
import pandas as pd


# Kkma 모듈 객체 선언
kkma = Kkma()

# 형태소 단위로 나눔
print(kkma.morphs(u'안녕하세요. 반갑습니다. 파이썬으로 크롤링하기'))
# 명사 추출
print(kkma.nouns(u'안녕하세요. 반갑습니다. 파이썬으로 크롤링하기'))
# 각 형태소의 품사를 분석
print(kkma.pos(u'안녕하세요. 반갑습니다. 파이썬으로 크롤링하기'))

# 문장단위?로 나누는 
okt = Okt()

# 형태소 단위로 나눔
print(okt.morphs(u'안녕하세요. 반갑습니다. 파이썬으로 크롤링하기'))
# 명사 추출
print(okt.nouns(u'안녕하세요. 반갑습니다. 파이썬으로 크롤링하기'))
# 각 형태소의 품사를 분석
print(okt.pos(u'안녕하세요. 반갑습니다. 파이썬으로 크롤링하기'))
# 정규화(약간의 맞춤법 교정)
print(okt.normalize(u'안녕하세욬ㅋㅋㅋㅋㅋ'))

text = "안녕하세요. 파이썬 입니다. 저는 파이썬을 배우고 있습니다. 사실 자바가 더 즐겁습니다. 크롤링은 재미있지만 썩 쉽게 느껴지지는 않습니다."
# 단어와 종류를 분리
for word, tag in kkma.pos(text):
    print(word, tag)
for word, tag in okt.pos(text):
    print(word, tag)

word_list = []
# 명사, 형용사만 따로 출력
for word, tag in okt.pos(text):
    if tag in ['Noun', 'Adjective'] : #명사만
        # print(word, tag)
        word_list.append(word)
print(word_list)

# Counter로 text 문장 수 출력
print(Counter(text))

text_list = ['파랑', '노랑', "빨강", '파랑', '초록', '빨강']
print(Counter(text_list))

print(Counter(word_list))