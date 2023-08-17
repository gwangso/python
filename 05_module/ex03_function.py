def vertical():
    for i in range(2,10):
        print(str(i)+"단")
        for j in range(1,10):
            print(i,"X",j,"=",i*j)

def horizontal():
    for i in range(2, 10):
        print(str(i)+"단")
        for j in range(1, 10):
            print(i,"X",j,"=",i*j, end="  ")
        print() 