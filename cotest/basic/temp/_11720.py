# src = https://www.acmicpc.net/problem/11720

## 틀림
## N = int(input())
## inputs = []
## inputs.append(list(map(int,input().split())))
## print(sum(inputs))

# import sys
# 
# # 첫째 줄: 숫자의 개수 N을 입력받습니다. (이 문제에서는 사실 N을 사용하지 않아도 됩니다. 둘째 줄 전체를 읽으면 되니까요.)
# N = int(sys.stdin.readline())
# 
# # 둘째 줄: N개의 숫자가 공백 없이 쓰여있는 문자열을 입력받습니다.
# # 예: "54321" 또는 "7000000000000000000000000"
# number_string = sys.stdin.readline().strip()
# 
# # 각 문자를 순회하며 숫자로 변환하고 합산합니다.
# total_sum = 0
# for char in number_string:
#     total_sum += int(char) # 각 문자를 정수로 변환하여 더함
# 
# # 또는 더 파이썬스러운 방법 (한 줄로)
# # total_sum = sum(map(int, number_string))
# 
# print(total_sum)


import sys
input = sys.stdin.readline
N = int(input())
num_string = input().strip()
# total = 0
# for char in num_string:
#     total += int(char)
print(sum(map(int, num_string)))