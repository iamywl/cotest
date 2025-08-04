# src = https://www.acmicpc.net/problem/1009
# 5
# 1 6
# 3 7
# 6 2
# 7 100
# 9 635


testcase = int(input())
inputs =  []

def finder(arg1, arg2):
    base = arg1%10
    if base == 0:
        return 10
    if base in [1,5,6]:
        return base
    if base in [4,9]:
        # case 4
        if arg2%2 == 0:
            return(base*base)%10
        # case 9
        else:
           return base
# 2 3 7 8
    if exp%4==0:
        exp=4
    return (base**exp)%10

for i in range(testcase):
    inputs.append(input().split())

for i in range(testcase):
    arg1, arg2 = map(int,inputs[i])
    print(finder(arg1,arg2))