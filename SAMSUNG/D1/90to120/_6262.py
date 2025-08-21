# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcVqFBK4-IDFAU4&categoryId=AWcVqFBK4-IDFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=4
input_string = input()
char_counts = {}
for char in input_string:
    char_counts[char] = char_counts.get(char, 0) + 1

sorted_keys = sorted(char_counts.keys())
#print(sorted_keys)
for key in sorted_keys:
    print(f"{key},{char_counts[key]}")