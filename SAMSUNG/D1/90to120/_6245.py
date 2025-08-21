# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcVCuAq4r4DFAU4&categoryId=AWcVCuAq4r4DFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=4
res = 0
while True:
    try:
        log = input()
        type, money = log.split()
        arg1 = int(money)
        if type == 'D':  
            res += arg1
        elif type == 'W': # W: 인출(Withdrawal)
            res -= arg1
    except EOFError:
        break

# 6. 모든 거래 내역 처리가 끝난 후, 최종 잔액을 형식에 맞춰 출력합니다.
print(f"잔액: {res}")