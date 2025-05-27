import sys
input = sys.stdin.readline

num1 = int(input())

for i in range(1,(num1+1)):
    a,b = map(int, input().split())
    print(f"Case #{i}: {a + b}")
