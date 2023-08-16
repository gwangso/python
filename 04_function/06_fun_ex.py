# 실행하면 콘솔에서 1또는 2를 입력받고 1은 세로형구구단, 2는 가로형구구단을 각각 출력한다.
# 구구단은 각각 함수로 정의하도록 한다.

def times_table(menu):
    if menu==1:
        print("세로형구구단")
        for i in range(2,10):
            print(str(i)+"단")
            for j in range(1,10):
                print(i,"x",j,"=",i*j)
    elif menu==2:
        for i in range(2,10):
            print(str(i)+"단")
            for j in range(1,10):
                print(i,"x",j,"=",i*j, end="  ")
            print()
    else:
        print("다음부턴 0부터 2중 선택하세요")

while True:
    print("1.세로출력 | 2.가로출력 | 0.그냥 나가기")
    menu = int(input("메뉴 입력 => "))
    if menu==0:
        print("그냥 나가버리기")
        break
    else:
        times_table(menu)