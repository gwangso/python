#튜플
#소괄호에 담는다
int_tuple = (1, 2, 3, 4)
print(int_tuple)
print(int_tuple[1])
print(int_tuple[3])
#int_tuple[2]=10
print(int_tuple[2])

str_tuple = ("hello", "안녕하세요", "ㅎㅎㅎ")

mix_tuple = (1,3,"ㅎㅎㅎ", "파이썬")

tuple_in_tuple = ("안녕", (1,10,"ㅎㅎㅎ"), "hello", 1.23)

print(tuple_in_tuple)

tuple_in_list = ["안녕", (1,50,"ㅎㅎㅎ"), "world", 5.31]
print(tuple_in_list)
tuple_in_list[1]=20
print(tuple_in_list)

list_in_tuple = ("안녕", [1,50,"ㅎㅎㅎ"], "world", 5.31)
print(list_in_tuple)
list_in_tuple[1][2] = 100
print(list_in_tuple)
list_in_tuple[1][1] = ""
print(list_in_tuple)