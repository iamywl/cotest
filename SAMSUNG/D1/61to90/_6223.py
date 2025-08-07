# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcU8f6a4kUDFAU4&categoryId=AWcU8f6a4kUDFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=3
# math 모듈을 import할 필요가 없습니다.
# import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def getArea(self):
        # 원주율을 3.14로 고정하여 계산합니다.
        return self.radius * self.radius * 3.14

# 반지름이 2인 객체 생성
circle = Circle(2)

# 면적 계산
area = circle.getArea()

# 출력 예시와 동일한 형식으로 결과 출력
print(f'원의 면적: {area}')