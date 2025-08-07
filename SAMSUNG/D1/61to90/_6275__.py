# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcVryq65BEDFAU4&categoryId=AWcVryq65BEDFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=3
# inputs = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
# print(inputs.replace('aeiou',''))

inputs = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
vowels = 'aeiouAEIOU' # 대소문자 모음 모두 포함

# 리스트 내포를 사용하여 모음이 아닌 문자들만 선택
result_list = [char for char in inputs if char not in vowels]

# 선택된 문자들을 하나의 문자열로 결합
output = ''.join(result_list)

print(output)