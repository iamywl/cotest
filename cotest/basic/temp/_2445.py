# src = https://www.acmicpc.net/problem/2445
import sys
input = sys.stdin.readline

N = int(input())

# 상단
for i in range(1,N+1):
    star    =   i
    space    =   (N-i) *2
    print(f"{'*' * star}{' ' * space}",end='')
    print(f"{'*' * star}")

# 상단
for i in range(1,N+1):
    star    =   N-i
    space   =   i*2  
    print(f"{'*' * star}{' ' * space}",end='')
    print(f"{'*' * star}")