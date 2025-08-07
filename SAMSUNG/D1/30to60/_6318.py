# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcWG7w65ZwDFAU4&categoryId=AWcWG7w65ZwDFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=2

# 'abcdef' 문자열을 키로 사용합니다.
keys = 'abcdef'

# 0부터 5까지의 정수를 값으로 사용합니다.
values = range(6)

# zip() 함수를 사용하여 키와 값을 묶고, dict() 함수로 딕셔너리를 생성합니다.
my_dict = dict(zip(keys, values))

# 딕셔너리의 각 키와 값을 반복문을 통해 출력합니다.
for key, value in my_dict.items():
    print(f'{key}: {value}')