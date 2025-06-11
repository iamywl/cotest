# src = https://www.acmicpc.net/problem/2439
import sys
input = sys.stdin.readline
N = int(sys.stdin.readline().strip())
for i in range(1, N + 1):
    print(' ' * (N - i) + '*' * i)