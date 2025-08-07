# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcU_1164n4DFAU4&categoryId=AWcU_1164n4DFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=3

inputs = input()
res = []
for chr in inputs:
    res.append(chr)
for i in range(0,len(inputs)+1//2):
    start = 0
    end = len(res)-1
    if res[start + (i)] != res[end -i]:
        print(f"입력하신 단어는 회문(Palindrome)아닙니다.")
        break
print(inputs)
print(f"입력하신 단어는 회문(Palindrome)입니다.")