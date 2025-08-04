# src =https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcUzTD64fcDFAU4&categoryId=AWcUzTD64fcDFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=2

class Student:
    def __init__(self, kor_score, eng_score, math_score):
        self.kor_score = kor_score
        self.eng_score = eng_score
        self.math_score = math_score
    def calculate_total(self):
        return self.kor_score + self.eng_score + self.math_score

kor, eng, math = 89, 90, 100
student1 = Student(kor, eng, math)
total_score = student1.calculate_total()
print(f"국어, 영어, 수학의 총점: {total_score}")