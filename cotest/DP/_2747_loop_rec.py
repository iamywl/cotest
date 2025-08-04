#src = https://www.acmicpc.net/problem/2747
def fin():
    N = int(input())

    cache = [0] * (N + 1)

    if N >= 0:
        cache[0] = 0
    if N >= 1:
        cache[1] = 1

    for i in range(2, N + 1):
        cache[i] = cache[i-1] + cache[i-2]
    print(cache[N])

fin()