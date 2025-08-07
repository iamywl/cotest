# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWc6XsuqxZoDFAWn&categoryId=AWc6XsuqxZoDFAWn&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=3


import sys


for line in sys.stdin:
    line = line.rstrip()  # 줄 끝 개행 제거
    if line == '':
        break
    print(f'>> {line.upper()}')

