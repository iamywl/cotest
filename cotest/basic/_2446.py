# # src = https://www.acmicpc.net/problem/2445
# import sys
# input = sys.stdin.readline
# 
# N = int(input())
# 
# # 상단
# for i in range(N):
#     star    = (2*N-1) - 2*i
#     space   = i
#     V = ' '
#     C = '*'
#     print(f"{V * space}{C * star}",end='')
#     print(f"{V * space}")
# # N = 5
# # i = 0 1 2 3 4 5
# # 9 7 5 3 1 
# # 0 1 2 3 4  
# 
# j = 0
# #  하단
# for i in range(N-2, -1, -1):
#     j = j + 1
#     star    = (2*N-1) - 2*j
#     space   = i  
#     S = ' '
#     C = '*'
#     #print(f"{space} : {star}")
#     print(f"{S * space}{C * star} {j}",end='')
#     print(f"{S * space}")

import sys

N = int(sys.stdin.readline())

for i in range(N):
    space = i
    star = (2 * N - 1) - (2 * i)
    print(' ' * space + '*' * star)

for i in range(N - 2, -1, -1):
    space = i
    star = (2 * (N - 1 - i) + 1)
    print(' ' * space + '*' * star)