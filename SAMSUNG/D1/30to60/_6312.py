# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AWcWDw965VEDFAU4&categoryId=AWcWDw965VEDFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=2

def multiply(*args):
    """
    가변 인자로 받은 정수들의 곱을 반환하는 함수.
    정수가 아닌 값이 포함되면 ValueError를 발생시킵니다.
    """
    result = 1
    for num in args:
        if not isinstance(num, int):
            raise ValueError("입력값 중 정수가 아닌 값이 있습니다.")
        result *= num
    return result

try:
    print(multiply(1, 2, 3))       # 올바른 입력
    print(multiply(1, 2, '4', 3))  # 잘못된 입력으로 인한 예외 발생
except ValueError as e:
    print(f"에러발생: {e}")