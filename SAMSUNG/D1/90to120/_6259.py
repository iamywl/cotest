# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcVoVgK48QDFAU4&categoryId=AWcVoVgK48QDFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=4
inputs = input()

# 문자와 숫자의 개수를 저장할 변수를 0으로 초기화합니다.
letter_count = 0
digit_count = 0

# 입력받은 문자열의 각 문자를 하나씩 순회합니다.
for char in inputs:
    # 현재 문자가 알파벳(a-z, A-Z)인지 확인합니다.
    if char.isalpha():
        # 알파벳이면 letter_count를 1 증가시킵니다.
        letter_count += 1
    # 현재 문자가 숫자인지 확인합니다.
    elif char.isdigit():
        # 숫자이면 digit_count를 1 증가시킵니다.
        digit_count += 1

# 정해진 형식에 맞춰 결과를 출력합니다.
print(f"LETTERS {letter_count}")
print(f"DIGITS {digit_count}")