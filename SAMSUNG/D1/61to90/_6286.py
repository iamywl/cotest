# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcV49NK5I4DFAU4&categoryId=AWcV49NK5I4DFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=3

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
fibo_list = [fib(i) for i in range(1, 11)]
print(fibo_list)