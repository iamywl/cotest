# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV189xUaI8UCFAZN&categoryId=AV189xUaI8UCFAZN&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=2&pageSize=30&pageIndex=1

#A 사의 경우:
    # 1리터당 P원의 돈을 지불해야한다.
#B 사의 경우:
    # W가  R이하일 경우 Q
    # W가 R초과일 경우 S*(W-R)리터

T = int(input())
def sol():
    P, Q, R, S, W = map(int, input().split())
    return f"{(min(case_a(P,W),case_b(Q,R,S,W)))}"

def case_a(P,W):
    return P*W

def case_b(Q,R,S,W):
    if W <= R:
        return(Q)
    else:
        return(Q+(S*(W-R)))

for i in range(1,T+1,1):
    print(f"#{i} {sol()}")

