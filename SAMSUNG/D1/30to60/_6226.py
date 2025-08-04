# src =https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcU-Vi64mUDFAU4&categoryId=AWcU-Vi64mUDFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=2

res = []
for i in range(1,200,1):
    if i % 7 == 0 and i % 5 != 0:
        res.append(str(i))
print(",".join(res))