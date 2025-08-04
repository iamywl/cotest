# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcVAYC64o8DFAU4&categoryId=AWcVAYC64o8DFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=2


res = []
for i in range(1, 100):
    if i % 2 !=0 :
        res.append(str(i))
print(", ".join(res))