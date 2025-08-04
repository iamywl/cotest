# # src = https://www.acmicpc.net/problem/2869
# 
# import sys
# input = sys.stdin.readline
# 
# A, B, V = map(int, input().split())
# 
# def up(arg):
#     return arg + A
# def down(arg):
#     return arg - B
# current = 0
# for i in range(1, V):
#     current = up(current)
#     if current == V:
#         print(f"{i}")
#         break
#     current = down(current)

import sys
import math

input = sys.stdin.readline

A, B, V = map(int, input().split())

if A >= V:
    print(1)
else:
    days = math.ceil((V - A) / (A - B)) + 1
    print(days)