# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcU-ky64mkDFAU4&categoryId=AWcU-ky64mkDFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=3

# 부모 클래스 Shape 정의
class Shape:
    # 기본 area 메서드 (0 반환)
    def area(self):
        return 0

# Shape 클래스를 상속받는 Square 자식 클래스 정의
class Square(Shape):
    # 생성자: length 필드를 초기화
    def __init__(self, length):
        self.length = length
    
    # 부모 클래스의 area 메서드를 오버라이딩
    def area(self):
        # 정사각형의 면적 (length * length) 반환
        return self.length * self.length

# 길이가 3인 Square 객체 생성
square = Square(3)

# area 메서드를 호출하여 면적 계산
result = square.area()

# 출력 예시와 동일한 형식으로 결과 출력
print(f'정사각형의 면적: {result}')
