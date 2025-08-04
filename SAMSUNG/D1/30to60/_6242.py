# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcVBCHq4qcDFAU4&categoryId=AWcVBCHq4qcDFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=2


inputs = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
blood_type_counts = {}

for blood_type in inputs:
    if blood_type in blood_type_counts:
        blood_type_counts[blood_type] += 1
    else:
        blood_type_counts[blood_type] = 1

print(blood_type_counts)