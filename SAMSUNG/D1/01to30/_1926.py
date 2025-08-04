# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5PjKXKALcDFAUq&categoryId=AV5PjKXKALcDFAUq&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=1
arg1, arg2 = map(int, input().split())

# 가위 1 
# 바위 2
# 보  3

# 가위 보
if arg1 == 1 and arg2 == 3: 
    print('A')
# 보 바위
elif arg1 == 3 and arg2 == 2:
    print('A')
# 바위 보
elif arg1 == 2 and arg2 == 3:
    print('A')

else:
    print('B')
