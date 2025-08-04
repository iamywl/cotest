# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcU9v3a4lgDFAU4&categoryId=AWcU9v3a4lgDFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=2



inputs = input()


# 대문자 => 소문자
if ord(inputs) >= 65 and ord(inputs) <= 90:
    #print(chr(ord(inputs)+32))
    print(f'{inputs}(ASCII: {ord(inputs)}) => {chr(int(ord(inputs)+32))}(ASCII: {ord(inputs)+32})')
 
# 소문자 => 대문자
if ord(inputs) >= 97 and ord(inputs) <= 122:
    #print(chr(ord(inputs)-32))
    print(f'{inputs}(ASCII: {ord(inputs)}) => {chr(ord(inputs)+32)}(ASCII: {ord(inputs)-32})')
# 아닌 것은 그대로 
else:
    print(inputs)
# ord(inputs)
# print(f'c(ASCII: 99) => C(ASCII: 67)')
# print(chr(ord('A')+32))
# print(ord('z'))