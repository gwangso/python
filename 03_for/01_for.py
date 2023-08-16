# range를 이용하여 순차적으로 숫자 출력

for i in range(10):
    print(i)

print()

for i in range(5, 12):
    print(i)

for i in range(1,6):
    print("*"*i)

for i in range(1,6):
    print(" "*(5-i)+"*"*i)

for i in range(1,6):
    print(" "*(6-i)+ "*"*(((i-1)*2)+1))