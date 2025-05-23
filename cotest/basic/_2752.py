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
