# src =https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcWGQF65YMDFAU4&categoryId=AWcWGQF65YMDFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=3

# numbers = list(range(1, 11))
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# squared_even_numbers = list(map(lambda x: x**2, even_numbers))
# print(squared_even_numbers)

inputs = list(range(1, 11))
res = []

# inputs 리스트의 각 항목에 대해 반복
for i in inputs:
    # 짝수인 경우
    if i % 2 == 0:
        # 제곱 값을 리스트에 추가
        res.append(i * i)
print(res)
