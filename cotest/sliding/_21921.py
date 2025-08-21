# src = https://www.acmicpc.net/problem/21921
import sys

input = sys.stdin.readline
n, x = map(int, input().split())
visit = list(map(int, input().split()))

if max(visit) == 0:
    print("SAD")
else:
    currnet = 0
    for i in range(x):
        currnet += visit[i]

    max_sum = currnet
    cnt = 1

    for i in range(x, n):
        currnet = currnet - visit[i - x] + visit[i]
        
        if currnet > max_sum:
            max_sum = currnet
            cnt = 1
        elif currnet == max_sum:
            cnt += 1
            
    print(max_sum)
    print(cnt)