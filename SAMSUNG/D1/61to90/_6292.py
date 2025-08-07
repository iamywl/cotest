# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcV8H3K5MkDFAU4&categoryId=AWcV8H3K5MkDFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=3

inputs = list(map(int,(input().split(","))))

print(inputs)
print(tuple(inputs))


# inputs = map(int,(input().split(",")))
# 
# map 은 1회용 오브젝트이다
# map은 입력된 문자열을 숫자로 바꾸어줄 이터레이터를 생성한다.
# 아직 숫자로 바뀌진않음.
# 
# input()함수를 이용하여 입력값을 받고 split(",")함수로 입력값 구분
# print(list(inputs)) 에서 inputs값을 사용
# print(list(inputs))
# 이터레이러를 모두 사용하여서 따라서 아래 코드는 동작하지 않음
# print(tuple(inputs))

