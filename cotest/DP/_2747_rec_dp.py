# src = https://www.acmicpc.net/problem/2747

cache = [0] * (45 + 1)
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if cache[n] != 0:
        return cache[n]
    cache[n] = fib(n - 1) + fib(n - 2)
    return cache[n]
n = int(input())
print(fib(n))