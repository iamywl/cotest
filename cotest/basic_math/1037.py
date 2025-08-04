#src = https://www.acmicpc.net/problem/1037
import sys
input=sys.stdin.readline

count = int(input())
inputs = list(map(int,input().split()))

print(max(inputs) * min(inputs))