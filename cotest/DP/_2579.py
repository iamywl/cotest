# src = https://www.acmicpc.net/submit/2579
import sys
def solve():
    N = int(sys.stdin.readline())
    stairs = [0] * (N + 1) 
    for i in range(1, N + 1):
        stairs[i] = int(sys.stdin.readline())
    dp = [0] * (N + 1)
    if N >= 1:
        dp[1] = stairs[1]
    if N >= 2:
        dp[2] = stairs[1] + stairs[2]
    for i in range(3, N + 1):
        dp[i] = max(dp[i-2], dp[i-3] + stairs[i-1]) + stairs[i]
    print(dp[N])
solve()
