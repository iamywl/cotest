# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcWFZL65W4DFAU4&categoryId=AWcWFZL65W4DFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=3
inputs = list(range(1, 11))

#짝수만 필터링해서 리스트에 저장하기
even_numbers = list(filter(lambda x: x %2 == 0, inputs))

print(even_numbers)