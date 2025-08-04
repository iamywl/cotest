# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcVAHLq4oMDFAU4&categoryId=AWcVAHLq4oMDFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=4
res = []
for i in range(1,101,1):
    if i%2 == 0:
        res.append(str(i))
print(" ".join(res))

