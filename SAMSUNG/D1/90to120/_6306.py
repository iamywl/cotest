# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcWA1Fa5SMDFAU4&categoryId=AWcWA1Fa5SMDFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=4
# 반목문에서 x, y 두 수를 입력 받아 두 수의 곱을 출력하고 종료하는 프로그램을 작성합니다.
# 만일 문자를 입력 받게 되면 "숫자가 아닙니다. 재입력하세요."라는 메시지를 출력한 뒤
# 다시 입력 받도록 합니다.



while True:
    inputs = input()
    if inputs.isalpha():
        print('숫자가 아닙니다. 재입력하세요.')
    if inputs.isdigit():