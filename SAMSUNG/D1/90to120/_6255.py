# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcVJZ964z0DFAU4&categoryId=AWcVJZ964z0DFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=4


products = {
    "TV": 2000000,
    "냉장고": 1500000,
    "책상": 350000,
    "노트북": 1200000,
    "가스레인지": 200000,
    "세탁기": 1000000,
}
res = sorted(products.items(), key=lambda item: item[1], reverse= True) 
#print(res)

# 정렬된 결과를 형식에 맞게 출력합니다.
for arg1, arg2 in res:
    print(f"{arg1}: {arg2}")