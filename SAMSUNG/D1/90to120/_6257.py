# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcVmIXq464DFAU4&categoryId=AWcVmIXq464DFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=4

# fruit = ['   apple    ','banana','  melon']
# res = { }
# key = {len(inputs) for inputs in fruit}

fruit = ['   apple    ', 'banana', '  melon']
res = {ans.strip(): len(ans.strip()) for ans in fruit} 
#test = {1:2}
#print(test)
print(res)