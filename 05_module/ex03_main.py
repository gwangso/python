# 구구단 함수를 ex03_function.py에 각각 정의
# main에서 1,2번 선택을 받아 세로형, 가로형을 각각 출력

import ex03_function
run = True
while run:
    print("1.세로 | 2.가로 | 0.종료")
    menu = int(input("메뉴 입력 > "))
    if menu==1:
        ex03_function.vertical()
    elif menu==2:
        ex03_function.horizontal()
    elif menu==0 :
        break
    else :
        print("다시선택")