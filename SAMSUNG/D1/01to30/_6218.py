# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcU7_G64j0DFAU4&categoryId=AWcU7_G64j0DFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=1


inputs = int(input())
for div in range(1,inputs+1):
    if inputs % (div) == 0:
        print(f'{div}(은)는 {inputs}의 약수입니다.')