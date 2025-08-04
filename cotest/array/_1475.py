# src = https://www.acmicpc.net/problem/1475

import math
import sys

inputs = sys.stdin.readline().strip()
counts = [0] * 10
for char_digit in inputs:
    digit = int(char_digit) 
    if digit == 9:
        counts[6] += 1
    else:
        counts[digit] += 1
res = []
for i in range(len(counts)):
    if i == 6:
        res.append(math.ceil(counts[6]/2))
    else:
        res.append(counts[i])
print(f"{int(max(res))}")
