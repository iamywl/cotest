# src = https://www.acmicpc.net/problem/2445

import sys
input = sys.stdin.readline
N = int(input())


for i in range(1,2*N+1):
    print(i)

# src = https://www.acmicpc.net/problem/2444

import sys
input = sys.stdin.readline
N = int(input())

# 상단 피라미드
for i in range(1, N + 1):
    spaces = N - i
    stars = 2 * i - 1
    print(' ' * spaces + '*' * stars)

# 하단 피라미드
for i in range(N - 1, 0, -1): # N-1부터 1까지 역순으로
    spaces = N - i
    stars = 2 * i - 1
    print(' ' * spaces + '*' * stars)