# src = https://www.acmicpc.net/problem/2587
import sys
input = sys.stdin.readline
#inputs = list(map(int, input().split())) 
inputs = []
for i in range(5):
    inputs.append(int(input()))
avg = (sum(inputs)//len(inputs))
temp = sorted(inputs) 
print(avg)
print(temp[2])


