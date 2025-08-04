# src = https://www.acmicpc.net/problem/2747

def fin(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            next_fib = a + b
            a = b
            b = next_fib
        return b
N = int(input())
print(fin(N))