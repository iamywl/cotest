#src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AWTLXCuapdcDFAVT&categoryId=AWTLXCuapdcDFAVT&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=30&pageIndex=1&&&&&&&&&&
T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    v = list(map(int, input().split()))
    end = 0
    sum_v= []
    for i in range(0 , N):
        if i+M > N:
            break
        sum_v.append(sum(v[i:i+M]))
        # print(f'i: {i} {sum_v} N : {N}')
    print(f'#{tc} {max(sum_v)-min(sum_v)}')

