# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcU5ILq4ggDFAU4&categoryId=AWcU5ILq4ggDFAU4&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=1

# 인치(inch)를 센티미터(cm)으로 변환하는 프로그램을 작성하십시오.
# 이 때 1 인치는 2.54 센티미터입니다.
inch = float(input().strip())
print(f"{inch:.2f} inch => {inch*2.54} cm")