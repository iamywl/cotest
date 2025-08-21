# src =https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AWTQSs6qQL0DFAVT&categoryId=AWTQSs6qQL0DFAVT&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=2&pageSize=10&pageIndex=2

T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    counts = {}
    for char in str1:
        counts[char] = 0
        
    for char in str2:
        if char in counts:
            counts[char] += 1
    
    max_count = 0
    for count in counts.values():
        # print(f"{counts.keys()}:{counts.values()}")
        if count > max_count:
            max_count = count
    print(f'#{tc} {max_count}')
