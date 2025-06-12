# src = https://www.acmicpc.net/problem/2443
import sys
input = sys.stdin.readline
N = int(sys.stdin.readline().strip())

for i in range(0,N):
    space   =  i
    star    = 2*N-(2*i+1) 
    print(f"{space * " "}", end= "")
    print(f"{star * "*"}")

    # print(f"space : {space}")
    # print(f"star : {star}")
