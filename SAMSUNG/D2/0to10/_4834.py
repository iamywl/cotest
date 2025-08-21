# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AWTLVouKpUgDFAVT&categoryId=AWTLVouKpUgDFAVT&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=30&pageIndex=1

T = int(input())

for tc in range(1,T+1):
    # N값의 범위는 5 ~ 100
    N = int(input())
    arr = input()
    int_arr =[]
    cnt = [0]*10
    digit=0
    for el in arr:
        # print(el)
        # print(cnt)
        cnt[int(el)] +=1
        int_arr.append(int(el))
        maxium = max(cnt)
    for i in range(len(cnt)-1,-1,-1):
        if cnt[i] == maxium:
            digit = i
            break

    print(f'#{tc} {digit} {maxium}')