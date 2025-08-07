# src =https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcVsKZq5B0DFAU4&categoryId=AWcVsKZq5B0DFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=3

# 다음의 결과와 같이 구구단 2단부터 9단의 결과값 중에 3의 배수거나 7의 배수인 수를

# 제외한 값을 리스트 객체 result 안에 각 단마다 리스트를 만들어 삽입하고 이를 출력하십시오.


result = []
for i in range(2, 10):
    temp_list = []
    for j in range(1, 10):
        if (i * j) % 3 != 0 and (i * j) % 7 != 0:
            temp_list.append(i * j)
    result.append(temp_list)

print(result)