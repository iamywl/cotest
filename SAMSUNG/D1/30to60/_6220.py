# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcU9JPq4k8DFAU4&categoryId=AWcU9JPq4k8DFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=1


inputs = int(input())
chr = input()

for i in range(1, inputs+1):
    if 96 < ord(chr) and ord(chr) < 123:
        print(f"#{i} {chr} 는 소문자 입니다.")
    else:
        print(f"#{i} {chr} 는 대문자 입니다.")

    # print(ord('a')) => 97
    # print(ord('z')) => 122
    # print(ord('A')) => 65
    # print(ord('Z')) => 90

