# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcV0Ll65EMDFAU4&categoryId=AWcV0Ll65EMDFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=3

numbers = [int(input()) for _ in range(5)]
average = sum(numbers) / len(numbers)
print(f'입력된 값 {numbers}의 평균은 {average}입니다.')