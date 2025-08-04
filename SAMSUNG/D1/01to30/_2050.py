# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&problemLevel=2&contestProbId=AV5QLGxKAzQDFAUq&categoryId=AV5QLGxKAzQDFAUq&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=2&pageSize=30&pageIndex=1

inputs = input()


#print(ord('A'))
for char in inputs:
    print(f"{ord(char) - 64}",end=' ')

