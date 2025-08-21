# src =https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcV7L7q5LEDFAU4&categoryId=AWcV7L7q5LEDFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=4

while True:
    inputs = input()
    if inputs == "종료":
        break
    else:
        res = [f'{inputs} * {i}  = {int(inputs) * i} 'for i in range(1, 10)]
        print(res)