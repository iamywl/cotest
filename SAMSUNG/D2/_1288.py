# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&problemLevel=2&contestProbId=AV18_yw6I9MCFAZN&categoryId=AV18_yw6I9MCFAZN&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=2&pageSize=30&pageIndex=1

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    seen_digits = set()
    k = 0
    current_sheep_number = 0
    while len(seen_digits) < 10:
        k += 1
        current_sheep_number = N * k
        for digit_char in str(current_sheep_number):
            seen_digits.add(int(digit_char))
    print(f'#{test_case} {current_sheep_number}')