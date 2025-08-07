# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcV1mla5GIDFAU4&categoryId=AWcV1mla5GIDFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=3

inputs = int(input())
def sol(args):
    res = []
    for div in range(1, args+1):
        if args % div == 0:
            res.append(div)
    return res
print(sol(inputs))