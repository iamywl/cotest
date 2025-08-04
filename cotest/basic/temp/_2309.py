# src = https://www.acmicpc.net/problem/2309
import sys
input = sys.stdin.readline
inputs = []
for _ in range(9):
    inputs.append(int(input().strip()))
total_sum = sum(inputs)
res = []

for i in range(9):
    for j in range(i + 1, 9):
        if (total_sum - inputs[i] - inputs[j]) == 100:
            for k in range(9):
                if k != i and k != j:
                    res.append(inputs[k])
            break
    if len(res) == 7:
        break
res.sort()

for dwarf_height in res:
    print(dwarf_height)