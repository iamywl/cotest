# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcWMsaK5eYDFAU4&categoryId=AWcWMsaK5eYDFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=2


def countdown(arg1):
    if arg1 <= 0:
        print('카운트다운을 하려면 0보다 큰 입력이 필요합니다.')
    for i in range(arg1,0,-1):
        print(i)
countdown(0)        
countdown(10)