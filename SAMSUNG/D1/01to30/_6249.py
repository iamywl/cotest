# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&problemLevel=2&contestProbId=AWcVDjz64tYDFAU4&categoryId=AWcVDjz64tYDFAU4&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=2&pageSize=10&pageIndex=1



inputs = input() 

counting = [0]*10

for char in inputs:
    digit = int(char)
    counting[digit] +=1
print("0 1 2 3 4 5 6 7 8 9")
print(*counting)


