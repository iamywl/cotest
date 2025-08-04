# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&problemLevel=2&contestProbId=AV5Pw_-KAdcDFAUq&categoryId=AV5Pw_-KAdcDFAUq&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=2&pageSize=30&pageIndex=1

testcase = int(input())




def sol():
    inputs = list(map(int, input().split()))
    res = (sum(inputs) - max(inputs) - min(inputs))/8
    return(res)


for num in range(1, testcase+1):
    print(f"#{num} {sol():.0f}" )