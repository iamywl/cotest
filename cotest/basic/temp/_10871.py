#src = https://www.acmicpc.net/problem/10871
#10 5
#1 10 4 9 2 3 8 5 7 6

import sys
input = sys.stdin.readline

a, x = map(int, input().split())

array = list(map(int, input().split()))

for num in array:
    if num < x:
        print(num, end=' ')
