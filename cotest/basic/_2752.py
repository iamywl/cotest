#https://www.acmicpc.net/problem/2752

import sys

input = sys.stdin.readline

boo = list(map(int, input().split()))
temp = int()

if (boo[0] > boo[1]):
    temp = boo[0]
    boo[0] = boo[1]
    boo[1] = temp

if (boo[1] > boo[2]):
    temp = boo[1]
    boo[1] = boo[2]
    boo[2] = temp

if (boo[0] > boo[1]):
    temp = boo[0]
    boo[0] = boo[1]
    boo[1] = temp

print(f"{boo[0]}, {boo[1]}, {boo[2]}")

# 파이썬은 sorting 라이브러리를 제공한다 ㅋㅋㅋ
# A = list(map(int, input().split()))
# A.sort()
# print(A[0], A[1], A[2])