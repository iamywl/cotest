# src = https://www.acmicpc.net/problem/2576
import sys
input = sys.stdin.readline

nums = [int(input()) for _ in range(7)]
mins = []

def prefix_sum(arg):
    sum_s = 0
    global mins
    for i in range(len(arg)):
        if arg[i] % 2 != 0:
            mins.append(arg[i])
            sum_s += arg[i]
    return sum_s

total = prefix_sum(nums)

if mins:
    print(total)
    print(min(mins))
else:
    print(-1)

