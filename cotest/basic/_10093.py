# src = https://www.acmicpc.net/problem/10093

# 숫자가 클경우를 고려해야한다.
# num1, num2 = map(int,input().split())
# print(f"{abs(num2-num1-1)}")
# for i in range(num1+1, num2):
#     print(f"{i}", end=' ')
# print()

num1, num2 = map(int, input().split())
if num1 > num2:
    num1, num2 = num2, num1
count = max(0, num2 - num1 - 1)
print(count)
if count > 0:
    for i in range(num1 + 1, num2):
        print(f"{i}", end=' ')
    print() # 숫자들 출력 후 줄바꿈