# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcVDLya4swDFAU4&categoryId=AWcVDLya4swDFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=4

inputs = input()
res = []
for i in range(len(inputs)):
    if i%2 == 0:
        res.append(inputs[i])

print("".join(res))
# 이게 좀 더 파이썬스러움
# print(inputs[::2])
