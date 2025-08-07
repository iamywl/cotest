# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcV2SNq5GwDFAU4&categoryId=AWcV2SNq5GwDFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=3

inputs = [1, 3, 11, 15, 23, 28, 37, 52, 85, 100]


res =[res for res in inputs if res % 2 == 0] 
print(res)