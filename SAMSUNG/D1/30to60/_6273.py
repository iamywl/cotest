# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcVqgVK4-YDFAU4&categoryId=AWcVqgVK4-YDFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=2


# 학생들의 점수를 튜플로 저장하고, 튜플을 항목으로 갖는 리스트를 생성합니다.
scores = [(90, 80), (85, 75), (90, 100)]

# enumerate 함수를 사용해 인덱스와 값을 함께 가져와 더 효율적으로 처리합니다.
# for student_num, student_scores in enumerate(scores):
# 아래 코드에서는 문제 요구사항에 따라 1번 학생부터 시작하도록 for-range를 사용했습니다.

for i in range(len(scores)):
    # 현재 학생의 번호는 인덱스에 1을 더한 값입니다.
    student_num = i + 1
    
    # 해당 학생의 튜플 점수를 가져옵니다.
    student_scores = scores[i]
    
    # 튜플의 두 점수를 더해 총점을 계산합니다.
    total_score = student_scores[0] + student_scores[1]
    
    # 총점을 2로 나누어 평균을 계산합니다.
    # 실수형으로 나누기 위해 / 연산자를 사용합니다.
    average_score = total_score / 2
    
    # f-string을 이용해 문제에서 요구하는 형식으로 결과를 출력합니다.
    print(f"{student_num}번 학생의 총점은 {total_score}점이고, 평균은 {average_score}입니다.")
