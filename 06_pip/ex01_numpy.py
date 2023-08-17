# numpy import
import numpy as np

# numpy 배열 선언
arr = np.array([2, 1, 5, 3, 4, 7, 9, 8, 6])
print(arr)

# 정렬
arr = np.sort(arr)
print(arr)

# 2개의 배열을 합침
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
arr3 = np.concatenate((arr1, arr2, [9]))
print(arr3)

# 배열 연산
arr11 = arr1 + 10
print("arr11 =", arr11)
arr12 = arr2 - arr1
print("arr12 =",arr12)

# 배열 슬라이싱(특정 인덱스 범위 접근하기)
arr4 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(arr4[:2]) # 0~1번 인덱스 (1, 2)
print(arr4[1:2]) # 1~1번 인덱스(2)
print(arr4[3:8]) # 3~7번 인덱스(4,5,6,7,8)
print(arr4[6:]) # 6~마지막(9번)인덱스(7,8,9,10)

arr5= np.array(["가", "나", "다"])
arr6= np.array(["a", "b", "c"])
print(arr5)
arr5 = arr5 + arr6
print(arr5)