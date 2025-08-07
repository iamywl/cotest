# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcU7di64jIDFAU4&categoryId=AWcU7di64jIDFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=3

class Student:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"이름: {self.name}"
class GraduateStudent(Student):
    def __init__(self, name, major):
        super().__init__(name)
        self.major = major
    def __str__(self):
        return f"{super().__str__()}, 전공: {self.major}"

student1 = Student("홍길동")
print(student1)
graduate_student1 = GraduateStudent("이순신", "컴퓨터")
print(graduate_student1)