# https://www.acmicpc.net/problem/2562

import sys
input = sys.stdin.readline

inputs = [int(input()) for _ in range(9)]

def isMax(arg):
    for i in range(9):
        # print("i 값:",i)
        if inputs[i] == max(inputs):
            return i +1
# print(max(inputs),'\n',isMax(inputs))
print(f"{max(inputs)}\n{isMax(inputs)}")