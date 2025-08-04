# src = https://www.acmicpc.net/problem/1026
import sys

# 5
# 1 1 1 6 0
# 2 7 8 3 1

def solve_treasure():
    N = int(sys.stdin.readline()) # 첫째 줄에서 N을 읽습니다.
    A = list(map(int, sys.stdin.readline().split())) 
    B = list(map(int, sys.stdin.readline().split()))

    # N = 5
    # A = [1, 1, 1, 6, 0]
    # B = [2, 7, 8, 3, 1]

    #       가장 작은 수와 가장 큰 수를 곱하면 최소화
    # B는 위치 바꿀 수 없음. -> A를 소팅 작은거 -> 큰순
    A.sort()
    # 코드: B.sort(reverse=True)는 B를 제자리에서 내림차순 정렬
    B.sort(reverse=True)
    # sorted B: [8, 7, 3, 2, 1]

    min_S = 0

    for i in range(N):
        #  곱 값 누계합.
        min_S += A[i] * B[i]
        
        #print(f"i={i}: A[{i}]={A[i]}, B[{i}]={B[i]}, 곱셈 결과={A[i]*B[i]}, 현재 min_S={min_S}")
    # i=0: A[0]=0, B[0]=8, 곱셈=0, min_S=0
    # i=1: A[1]=1, B[1]=7, 곱셈=7, min_S=0+7=7
    # i=2: A[2]=1, B[2]=3, 곱셈=3, min_S=7+3=10
    # i=3: A[3]=1, B[3]=2, 곱셈=2, min_S=10+2=12
    # i=4: A[4]=6, B[4]=1, 곱셈=6, min_S=12+6=18

    print(min_S)
if __name__ == "__main__":
    solve_treasure()