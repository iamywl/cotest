# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AZD8K_UayDoDFAVs
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