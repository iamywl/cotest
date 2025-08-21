# srt = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AWTQRytKQJ0DFAVT&categoryId=AWTQRytKQJ0DFAVT&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=2&pageSize=10&pageIndex=2
T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    if str1 in str2:
        result = 1
    else:
        result = 0
    print(f"#{tc} {result}")