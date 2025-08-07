# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcWAjaa5RkDFAU4&categoryId=AWcWAjaa5RkDFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=3


inputs = [12,24,35,24,88,120,155,88,120,155]

def notdup (args):
    res = list(set(args))
    return res
print(notdup(inputs))