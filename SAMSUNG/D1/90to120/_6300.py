# src =https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcV_Vj65QMDFAU4&categoryId=AWcV_Vj65QMDFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=4

inputs = [12, 24, 35, 70, 88, 120, 155]
res = [val for idx, val in enumerate(inputs) if idx %2 != 0]

print(res)