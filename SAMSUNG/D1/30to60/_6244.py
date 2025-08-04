# 
# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcVCgj64roDFAU4&categoryId=AWcVCgj64roDFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=2



inputs = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
total = 0

while inputs:
    score = inputs.pop()
    if score >= 80:
        total += score

print(total)