# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcU-yn64m4DFAU4&categoryId=AWcU-yn64m4DFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=2


result = []
for number in range(100, 301):
    hundreds_digit = number // 100
    tens_digit = (number // 10) % 10
    ones_digit = number % 10

    if hundreds_digit % 2 == 0 and tens_digit % 2 == 0 and ones_digit % 2 == 0:
        result.append(str(number))

print(",".join(result))