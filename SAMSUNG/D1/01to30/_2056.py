# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QLkdKAz4DFAUq&categoryId=AV5QLkdKAz4DFAUq&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=1

days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

T = int(input())

for t in range(1, T + 1):
    date_str = input()
    
    year = date_str[0:4]
    month = date_str[4:6]
    day = date_str[6:8]
    
    #year = int(year)
    #year = 0010일 경우 
    # int 로 타입캐스팅하면 101년이되어 3자리가된다.
    year = year
    month_int = int(month)
    day_int = int(day)
    
    result = "-1"
    
    if 1 <= month_int <= 12:
        if 1 <= day_int <= days_in_month[month_int]:
            result = f"{year}/{month}/{day}"
            
    print(f"#{t} {result}")