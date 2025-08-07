# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcU-MXK4mADFAU4&categoryId=AWcU-MXK4mADFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=3

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def getArea(self):
        return self.width * self.height
rectangle = Rectangle(4, 5)
area = rectangle.getArea()
print(f'사각형의 면적: {area}')

