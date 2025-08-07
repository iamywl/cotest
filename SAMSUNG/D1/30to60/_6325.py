# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcWJUGa5c0DFAU4&categoryId=AWcWJUGa5c0DFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=2
def finder(inputs, target):
    if target in inputs:
        print(f'{target} => True')
    else:
        print(f'{target} => False')
inputs = [2, 4, 6, 8, 10]

print(inputs)
finder(inputs,5)
finder(inputs,10)