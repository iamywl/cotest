# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcV1MO65FYDFAU4&categoryId=AWcV1MO65FYDFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=4

import random

old_list = [random.randint(1, 10) for _ in range(10)] # 랜덤 리스트 생성 시 사용
num = int(input())
new_list = []
for item in old_list:
    if item < num:
        new_list.append(item)
print(f'new_list: {new_list}')