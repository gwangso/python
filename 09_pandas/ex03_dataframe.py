import pandas as pd

scores1 = pd.DataFrame(
    [
        [96, 76,60,85,80], 
        [88,92,100,55,70],
        [10,20,30,40,50]
    ]
)
print(scores1)

scores2 = pd.DataFrame(
    [
        [96, 76,60,85,80], 
        [88,92,100,55,70],
        [10,20,30,40,50]
    ],
    index=["java", "python", "js"]
)
print(scores2)

student_number = [1,2,3,4,5]
scores3 = pd.DataFrame(
    [
        [96, 88, 10],
        [76, 92, 20],
        [60, 100, 30],
        [85, 55, 40],
        [80, 70, 50]
    ],
    index=student_number
)
print(scores3)

scores4 = pd.DataFrame(
    {
        "java" : [96, 76,60,85,80], 
        "python" :[88,92,100,55,70],
        "js" : [10,20,30,40,50]
    },
    index=student_number
)
print(scores4)

# 딕셔너리 데이터를 DataFrame으로 변환
scores_dict = {
    "java" : [96,76,60,85,80], 
    "python" :[88,92,100,55,70],
    "js" : [10,20,30,40,50]
}
scores5 = pd.DataFrame(scores_dict, index=student_number)
print(scores5)

# 이름 데이터 추가(Like Series하나 추가)
scores5["이름"] = ["김파이", "이파이", "박파이", "최파이", "정파이"]
print(scores5)

# 데이터 추가(Like 인덱스 하나가 추가)
scores5.loc[6] = [80, 80, 80, "조파이"]
print(scores5)

student_number=[1,2,3,4,5,6]
scores6 = pd.DataFrame(
    {
        "이름" : ["김파이", "이파이", "박파이", "최파이", "정파이", "조파이"],
        "java" : [96, 76, 60, 85, 80, 99], 
        "python" :[88, 92, 100, 55, 70, 56],
        "js" : [10, 20, 30, 40, 50, 60]
    },
    index=student_number
)#.transpose() 행열을 서로 바꿔줌
print(scores6)

# index 기준 내림차순 정렬
print(scores6.sort_index(ascending=False))
# 이름 기준 오름차순 정렬
print(scores6.sort_values(by="이름"))
# python 기준 내림차순 정렬
print(scores6.sort_values(by="python", ascending=False))

# 첫 2줄만 조회
print(scores6.head(2))
# 마지막 2줄만 조회
print(scores6.tail(2))

# DataFrame을 csv로 내보내기
scores6.to_csv("./scores.csv", encoding="UTF-8-sig") # 한글깨짐 방지 encoding="UTF-8-sig"