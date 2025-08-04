# src = https://www.acmicpc.net/problem/2442 
import sys
input = sys.stdin.readline
N = int(sys.stdin.readline().strip())
for i in range(0, N):
    print(' ' * i + '*' * (N-i))