# src =  https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5LrsUaDxcDFAXc&categoryId=AV5LrsUaDxcDFAXc&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=2&pageSize=30&pageIndex=1

T = int(input())

def sol(cnt, products):
    maxpriz = 0
    profit = 0
    for i in range(cnt-1, -1, -1):
        if products[i] > maxpriz:
            maxpriz = products[i]
        else:
            profit = profit +maxpriz - products[i]
    return profit    
    
for testnum in range(1, T+1):
    product_cnt = int(input())
    products = list(map(int, input().split()))
    print(f"#{testnum} {sol(product_cnt, products)}")

#    maxprice = 0
#    profit = 0
#    for i in range(len(products), -1, -1):
#        if products[i] > maxprice:
#            maxprice = products[i]
#        else:
#            profit = products[i] - maxprice