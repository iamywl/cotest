testcase = int(input())


def sol(arg1, arg2):
    return f"#{arg1} {max(arg2)} "

for case in range(1, testcase+1,1):
    inputs = list(map(int,input().split()))
    print(sol(case,inputs))


'''    
# 테스트 케이스의 개수 T를 입력받습니다.
T = int(input())

# T번만큼 반복합니다. test_case 변수에는 1, 2, 3, ... T가 차례로 들어갑니다.
for test_case in range(1, T + 1):
    # 공백으로 구분된 10개의 숫자를 입력받아 정수 리스트로 만듭니다.
    numbers = list(map(int, input().split()))
    
    # 내장 함수 max()를 이용해 리스트에서 가장 큰 값을 찾습니다.
    max_num = max(numbers)
    
    # f-string을 이용해 요구사항에 맞는 형식으로 출력합니다.
    print(f"#{test_case} {max_num}")
'''    