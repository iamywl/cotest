# src =https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AWTLcyA6qAMDFAVT&categoryId=AWTLcyA6qAMDFAVT&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=30&pageIndex=1

def binary_search_count(P, target_page):
    count = 0
    start = 1
    end = P
    
    while start <= end:
        count += 1
        middle = int((start + end) / 2)
        
        if middle == target_page:
            return count
        elif middle > target_page:
            end = middle
        else:
            start = middle
            
T = int(input())

for test_case in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())
    
    a_count = binary_search_count(P, Pa)
    b_count = binary_search_count(P, Pb)
    
    result = ''
    if a_count < b_count:
        result = 'A'
    elif b_count < a_count:
        result = 'B'
    else:
        result = '0'
        
    print(f'#{test_case} {result}')