# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcWHqK65awDFAU4&categoryId=AWcWHqK65awDFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=2

user1 = input()
user2 = input()
user1_arg = input()
user2_arg = input()

def sol(arg1, arg2, arg3, arg4):
# user2 win
    if user1_arg == '가위' and user2_arg == '바위':
        print(f"{user2_arg}가 이겼습니다!")
    if user1_arg == '바위' and user2_arg == '보':
        print(f"{user2_arg}가 이겼습니다!")
    if user1_arg == '보' and user2_arg == '가위':
        print(f"{user2_arg}가 이겼습니다!")

# user1 win
    if user1_arg == '가위' and user2_arg == '보':
        print(f"{user1_arg}가 이겼습니다!")
    if user1_arg == '바위' and user2_arg == '가위':
        print(f"{user1_arg}가 이겼습니다!")
    if user1_arg == '보' and user2_arg == '바위':
        print(f"{user1_arg}가 이겼습니다!")
sol(user1,user2,user1_arg,user2_arg)
#     if user1_arg == user2_arg:
#         print(f"{user2_arg}가 이겼습니다!")