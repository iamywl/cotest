# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcV8oTa5M0DFAU4&categoryId=AWcV8oTa5M0DFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=3
inputs = list(map(int,input().split(",")))
res = [i*i*3.14 for i in inputs]
output_string = ", ".join(map(str, res))
print(output_string)