# T개의 개수의 테스트 케이스가 주어진다.
# 각 테스트 케이스의 개수는 10개
# 각 테스트 케이스별로 평균 값을 출력하라

def avg(arg):
    average = int(sum(arg))/int(len(arg))
    return average 

T = int(input())
for i in range(1, T+1):
    inputs = list(map(int,input().split()))
    result = 0
    for j in range(0, T):
        result = avg(inputs)
    print(f" {i} {result}")