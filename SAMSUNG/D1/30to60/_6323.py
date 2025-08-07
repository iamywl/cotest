# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcWIgR65boDFAU4&categoryId=AWcWIgR65boDFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=2
def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [1]
    fib_list = [1, 1]
    for _ in range(n - 2):
        next_fib = fib_list[-1] + fib_list[-2]
        fib_list.append(next_fib)
    return fib_list
n = int(input())
result = fibonacci(n)
print(result)