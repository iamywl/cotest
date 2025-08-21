# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcVmn-647oDFAU4&categoryId=AWcVmn-647oDFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=4

inputs = int(input())

res = {}

for i in range(1, inputs+1):
    res[i] = i*i

print(res)