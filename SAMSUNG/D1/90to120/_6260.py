# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcVo2pa480DFAU4&categoryId=AWcVo2pa480DFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=4

# 97 ~ 122
# print(ord('a'))
# print(ord('z'))

inputs  = input()
upper   = 0 
lower   = 0 

for arg in inputs:
    #print(arg)
    if ord(arg) >= 97 and ord(arg) <= 122:
        lower   += 1 
    if ord(arg) >= 65 and ord(arg) <= 90:
        upper   += 1 

print(f'UPPER CASE {upper}')
print(f'LOWER CASE {lower}')