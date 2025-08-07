# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcWMay65eIDFAU4&categoryId=AWcWMay65eIDFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=2



def max_lenth(arg):
    if len(arg[0]) > len(arg[1]):
        return arg[0]
    if len(arg[0]) <= len(arg[1]):
        return arg[1]


inputs = input().split(",")

print(max_lenth(inputs))
