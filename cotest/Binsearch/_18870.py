# src = https://www.acmicpc.net/problem/18870 
import sys

input = sys.stdin.readline

def make_uniq(arg):
    #if !(coords): 이게 되나 싶은게 되고 이게 안되나 싶네 
    if not arg: 
        return []
    # sort list
    # 소팅해서 작은 부터 하나씩 비교해서 이전 값과 일치하면 유니크하지 않음을 판단함.
    arg.sort()
    uni_inputs = []
    uni_inputs.append(arg[0]) 
    for i in range(1, len(arg)):
        # f !(arg[i] == arg[i-1]) 이런거 안됨;; 
        if arg[i] != arg[i-1]:
            # uni_inputs[i] = coords[i] 이런거 안됨.
            uni_inputs.append(arg[i])
    return uni_inputs

def solve():
    N = int(input())
    inputs = list(map(int, input().split())) # original_coords -> inputs
    temp = list(inputs)
    uni_inputs = make_uniq(temp)
    result = [0] * N
    uni_inputs_cnt = len(uni_inputs)
    # 0 ~ N까지
    for i in range(N):
        target = inputs[i]
        low = 0
        # uni_inputs의 길이보다 하나 적은게 high의 index
        high = uni_inputs_cnt - 1
        index_found = -1
        # unique한 리스트에서 카운팅 해서 res에 따로 저장해줌
        while low <= high:
            # mid = (low + high) //2 정수 범위 오버 플로우 발생가능함.
            # 10 mid = 5 ||  high == low + high -low , LOL~
            mid = low + (high - low) // 2 
            if uni_inputs[mid] == target:
                index_found = mid
                break
            elif uni_inputs[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        result[i] = index_found
    for i in range(N):
        print(result[i], end=' ')
    print() 
solve()