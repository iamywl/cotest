# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcWL1iq5dkDFAU4&categoryId=AWcWL1iq5dkDFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=2

inputs = int(input())

def fac(arg1):
    if arg1 == 1:
        return 1
    else:
        return fac(arg1-1) * arg1
print(fac(inputs))