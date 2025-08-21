# src = https://www.acmicpc.net/problem/26091
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
abilities = list(map(int, input().split()))
abilities.sort()

left = 0
right = n - 1
count = 0

while left < right:
    if abilities[left] + abilities[right] >= m:
        count += 1
        left += 1
        right -= 1
    else:
        left += 1

print(count)