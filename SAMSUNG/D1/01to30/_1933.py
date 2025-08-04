# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5PhcWaAKIDFAUq&categoryId=AV5PhcWaAKIDFAUq&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=1

inputs = int(input())
res = []

for num in range(1,inputs+1,1):
    if inputs % num == 0:
        res.append(str(num))
print(" ".join(res))