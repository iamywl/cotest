# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5Pl0Q6ANQDFAUq&categoryId=AV5Pl0Q6ANQDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=2&pageSize=30&pageIndex=2&&&&&&&&&&


T = int(input())
N = int(input())
P = {2:0,3:0,4:0,5:0,7:0,11:0}

for tc in range(1,T+1):
    for i in P.keys():
        if N%i == 0:
            P.values(P.keys()) +=1
    print(f'#{tc} {P.values()}')

    