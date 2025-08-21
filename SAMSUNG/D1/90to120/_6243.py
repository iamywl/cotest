# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcVBy7q4rMDFAU4&categoryId=AWcVBy7q4rMDFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=4

inputs = input().split(" ")


res = sorted(set(inputs))

print(",".join(res))