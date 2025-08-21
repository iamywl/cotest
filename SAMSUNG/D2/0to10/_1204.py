# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV13zo1KAAACFAYh&categoryId=AV13zo1KAAACFAYh&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=2&pageSize=30&pageIndex=1
T = int(input())
for tc in range(1, T+1):
    res=[0]*101
    tc_num = int(input())
    inputs = list(map(int, input().split()))
    for i in inputs:
        res[i] +=1 
    mx = max(res)
    for idx in range(len(res)-1, -1, -1):
        if res[idx] == mx:
            print(f'#{tc_num} {idx}')

