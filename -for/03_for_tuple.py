tuple1 = (1,2,3,4)
for i in tuple1:
    print(i)

tuple2 = ("가", "나", "다", "라") 
for i in tuple2:
    print(i)

for i, j in zip(tuple1, tuple2):
    print(i, j)

