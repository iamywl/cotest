# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV2gbY0qAAQBBAS0&categoryId=AV2gbY0qAAQBBAS0&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=1
res = []
for i in range(int(input().strip()),-1,-1):
    res.append(i)
print(*res)


# # 입력받은 숫자부터 -1 직전(즉, 0)까지 1씩 감소
# for i in range(int(input()), -1, -1):
#   # end=" "를 이용해 숫자를 출력하고 한 칸 띄움
#   print(i, end=" ") 