# 실행하면 콘솔에서 1또는 2를 입력받고 1은 세로형구구단, 2는 가로형구구단을 각각 출력한다.
# 구구단은 각각 함수로 정의하도록 한다.

def vertical(num):
    print(str(num)+"단")
    for i in range(1, 10):
        print(num,"x",i,"=",num*i)

def horizon(num):
    print(str(num)+"단")
    for i in range(1,10):
        print(num,"x",i,"=",i*num, end="  ")
    print()

while (True):    
    print("1.세로출력 | 2.가로출력 | 0. 그만")
    menu = int(input("메뉴선택 => "))
    if menu==1:
        num = int(input("숫자입력 부탁 => "))
        vertical(num)
    elif menu==2:
        num = int(input("숫자입력 부탁 => "))
        horizon(num)
    elif menu==0:
        print("종료")
        break
    else :
        print("메뉴 위에 1, 2번 선택하라는거 보이죠? 다시선택하세요.")
    print()