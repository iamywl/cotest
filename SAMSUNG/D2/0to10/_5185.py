# src = https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

res =""
hex_char = '1'
decimal_num = int(hex_char, 16)
raw_binary = bin(decimal_num)# T = int(input())
print(raw_binary)
four_digit_binary = raw_binary[2:].zfill(4)
print(raw_binary[2:])
print(four_digit_binary)
res += four_digit_binary
print(res)

# 
# for test_case in range(1, T + 1):
#     N, hex_string = input().split()
#     
#     binary_result = ''
#     
#     for hex_char in hex_string:
#         decimal_num = int(hex_char, 16)
#         raw_binary = bin(decimal_num)
#         four_digit_binary = raw_binary[2:].zfill(4)
#         binary_result += four_digit_binary
#         
#     print(f"#{test_case} {binary_result}")

# # 다른 풀이 방법
# T = int(input())
# ## 16진수 각 문자에 해당하는 4자리 2진수 매핑 테이블
# hex_to_bin = {
#     '0': '0000', '1': '0001', '2': '0010', '3': '0011',
#     '4': '0100', '5': '0101', '6': '0110', '7': '0111',
#     '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
#     'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
# }
# 
# for test_case in range(1, T + 1):
#     N, hex_str = input().split()
#     
#     result = ""
#     for char in hex_str:
#         result += hex_to_bin[char]
#     
#     print(f'#{test_case} {result}')
# 
# T = int(input())
# hex = {'0': '0000'}
# for tc in range(T):
#     size , inputs = input().split()
#     for char in inputs:
#         res = ""
#         res += hex[char]
#     print(f'# {tc} {res}')
# 
# 