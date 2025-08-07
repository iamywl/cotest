# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcV15cq5GgDFAU4&categoryId=AWcV15cq5GgDFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=3


inputs = int(input())
res = [i for i in range(1, inputs+1) if inputs % i == 0]
print(res)
