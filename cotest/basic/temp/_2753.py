# src = https://www.acmicpc.net/problem/2753
# 
import sys
input = sys.stdin.readline

#Flase print(bool(8%4)) 0 
#True print(bool(9%4)) !0


var = int(input())

if(not(bool(var%4)) and (var%100) or not(bool((var%400)))):
    print(1)
else:
    print(0)
