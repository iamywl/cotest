# src = https://www.acmicpc.net/problem/1009
# 5
# 1 6
# 3 7
# 6 2
# 7 100
# 9 635
import sys
input = sys.stdin.readline

testcase = int(input())
inputs =  []

def suqr(arg1, arg2):
    return arg1**arg2
    

for i in range(testcase):
    inputs.append(input().split())

for i in range(testcase):
    arg1, arg2 = map(int,inputs[i])
    #print(f"suqr : {suqr(arg1, arg2)%10}")
    print(f"{suqr(arg1, arg2)%10}")
#print(inputs)