# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcVAtfa4p8DFAU4&categoryId=AWcVAtfa4p8DFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=2

res = 0
for i in range(1,100,1):
    if i % 3 == 0:
        res += i
print(f"1부터 100사이의 숫자 중 3의 배수의 총합: {res}")