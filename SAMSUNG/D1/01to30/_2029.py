#src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QGNvKAtEDFAUq&categoryId=AV5QGNvKAtEDFAUq&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=1


testcase = int(input())


def div(arg1, arg2):
    return arg1//arg2

def mod(arg1, arg2):
    return arg1%arg2

for testcase_num in range(1, testcase+1):
    arg1, arg2 = map(int, input().split())
    print(f'#{testcase_num} {div(arg1, arg2)} {mod(arg1, arg2)}')
    