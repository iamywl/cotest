# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcWMJsq5d4DFAU4&categoryId=AWcWMJsq5d4DFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=2
def square(arg):
    return arg*arg
inputs = input().split(',')
for i in inputs:
    print(f'square({int(i)}) => {square(int(i))}')