# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&problemLevel=2&contestProbId=AZD8K_UayDoDFAVs&categoryId=AZD8K_UayDoDFAVs&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=2&pageSize=10&pageIndex=1

#T = 5
#1 2 2
#1 2 3
#1 2 4
#1 2 5
#10 7 1293

# Test case가 주어지고
# x+=y
# y+=x
# 위 식을 이용하여 N을 초과하는 식을 작성하라

# gready
T = int(input())
for t in range(1, T + 1):
    x, y, N = map(int, input().split())
    
    count = 0
    while max(x, y) <= N:
        if x < y:
            x += y
        else:
            y += x
        count += 1
        
    print(f"{count}")