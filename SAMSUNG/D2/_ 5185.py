#src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AWTtiyIqd_wDFAVT&categoryId=AWTtiyIqd_wDFAVT&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=2&pageSize=30&pageIndex=2

testcase = int(input())

for n in range(n):
    N, hex_string = input().split()
    res =''

    for hex in hex_string:
        dec = int(hex, 16)
        rawbin = bin(dec)
        four_digit_bin = rawbin[2:].zfill(4)
        res += four_digit_bin

    f'# {n} {res}'