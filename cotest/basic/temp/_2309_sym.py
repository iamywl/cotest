# src = https://www.acmicpc.net/problem/2309

import sys
from itertools import combinations

input = sys.stdin.readline

inputs = []

for _ in range(9):
    inputs.append(int(input().strip()))

all_combinations_of_7 = combinations(inputs, 7)
#print(all_combinations_of_7)

res = []

for combination in all_combinations_of_7:
    if sum(combination) == 100:
        res = list(combination)
        break

res.sort()
#print(f"{res}")

for ans in res:
    print(ans)
    #print(f"ans:{ans}")