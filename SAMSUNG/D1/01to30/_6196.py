# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcUn02K4a0DFAU4&categoryId=AWcUn02K4a0DFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=2

inputs = int(input())

res = inputs + (inputs*10+inputs) + (inputs*100+inputs*10+inputs) + (inputs*1000+inputs*100+inputs*10+inputs)
print(res)


# inputs = int(input())
# res = 0
# for i in range(1, 5):
#     term = 0
#     for j in range(i):
#         term += inputs * (10 ** j)
#     res += term
# print(res)

