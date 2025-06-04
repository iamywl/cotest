# 2개의 수를 입력받아 크기를 비교하여 등호 또는 부등호를 출력하는 프로그램을 작성하라
T = int(input())
def compare(arg1, arg2):
    if arg1 > arg2:
        res = '>' 
        return res
    elif arg1 < arg2:
        res = '<' 
        return res
    else:
        res = '='
        return res
    
for i in range(0,T):
    inputs = list(map(int, input().split()))
    # print("i", i)
    # print("inputs :", inputs)
    print(f"#{i+1} {compare(inputs[0], inputs[1])}")