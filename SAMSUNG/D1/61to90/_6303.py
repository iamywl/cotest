# src =https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcWAPiq5REDFAU4&categoryId=AWcWAPiq5REDFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=3&&&&&&&&&&

list1 = [1, 3, 6, 78, 35, 55]
list2 = [12, 24, 35, 24, 88, 120, 155]
res = []

for i in list1:
    if i in list2:
        # 있다면 결과 리스트에 추가
        res.append(i)
print(res)