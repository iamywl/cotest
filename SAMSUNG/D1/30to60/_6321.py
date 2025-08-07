# src =https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcWH66K5bADFAU4&categoryId=AWcWH66K5bADFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=2



def sol(arg):
    prime = 0
    for i in range(1,arg+1,1):
        if arg % i == 0:
            prime +=1
    return prime

inputs = int(input())

if sol(inputs) == 2:
    print('소수입니다.')
else:
    print('소수가 아닙니다.')