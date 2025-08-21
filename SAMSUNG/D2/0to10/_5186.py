# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AWTtj7GqeAgDFAVT&categoryId=AWTtj7GqeAgDFAVT&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=30&pageIndex=1

def solve():
    N = float(input())
    binary = ""
    count = 0

    while N > 0 and count < 13:
        N *= 2
        if N >= 1:
            binary += "1"
            N -= 1
        else:
            binary += "0"
        count += 1

    if count >= 13:
        return "overflow"
    else:
        return binary

T = int(input())
for tc in range(1, T + 1):
    result = solve()
    print(f"#{tc} {result}")