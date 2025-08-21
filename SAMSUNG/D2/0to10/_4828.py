# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AWTLQZwKon4DFAVT&categoryId=AWTLQZwKon4DFAVT&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=30&pageIndex=1



T = int(input())


for tc in range(1,T+1):
    N = int(input())
    inputs = list(map(int, input().split()))
    res = max(inputs)- min(inputs) 
    print(f"#{tc} {res}")
    