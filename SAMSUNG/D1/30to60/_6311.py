# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcWDP9a5UYDFAU4&categoryId=AWcWDP9a5UYDFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=2



# 점수 규칙을 딕셔너리로 정의
score_rules = {'A': 4, 'B': 3, 'C': 2, 'D': 1}

# 문제에서 주어진 문자열
s = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"

# map 함수와 람다식을 이용해 각 문자를 점수로 변환
# lambda char: score_rules[char]는 문자열의 각 문자를 인자로 받아
# score_rules 딕셔너리에서 해당 문자의 점수를 찾아 반환하는 역할을 합니다.
# sum 함수를 이용해 점수들의 총합을 계산
# 결과 출력

scores = map(lambda char: score_rules[char], s)
total_score = sum(scores)
print(total_score)