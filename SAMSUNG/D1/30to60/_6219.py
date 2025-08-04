# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcU8gqq4kYDFAU4&categoryId=AWcU8gqq4kYDFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=1

inputs = int(input())



global cnt, res 
res =[]
cnt = 0

for div in range(1,inputs+1):
    if inputs%div==0:
        print(f"{div}(은)는 {inputs}의 약수입니다.")
        cnt += 1
        res.append(div)
if cnt == 2:
    print(f"{inputs}(은)는 {res[0]}과 {res[1]}로만 나눌 수 있는 소수입니다.")

