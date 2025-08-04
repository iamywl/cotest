'''
# src = https://www.acmicpc.net/problem/1267

def calYS(arg):
    total = 0
    for i in range(len(arg)):
        if arg[i] < 30:
            total = total + 10
        elif arg[i] >= 30 and arg[i] <60:
            total = total + 20
        elif arg[i] >= 60:
            total = total + 30
    return total

def calMS(arg):
    total = 0
    for i in range(len(arg)):
        if arg[i] < 60:
            total = total + 15
        elif arg[i] >= 60:
            total = total + 30
    return total

N = int(input())
inputs = list(map(int, input().split()))
    # input_arr.append(map(int, (input().split())))

# Y == M    
Y = calYS(inputs) # 40
M = calMS(inputs) #45
if (Y==M):
    print(f"Y M " + f"{Y}")
# Y > M     
elif (Y > M):
    print(f"M " + f"{M}")
# Y < M     
elif (Y < M):
    print(f"Y " + f"{Y}")
'''
def calYS(durations):
    total_cost = 0
    for d in durations:
        # 영식 요금제: (통화시간 // 30 + 1) * 10
        cost_for_call = (d // 30 + 1) * 10
        total_cost += cost_for_call
    return total_cost

def calMS(durations):
    total_cost = 0
    for d in durations:
        # 민식 요금제: (통화시간 // 60 + 1) * 15
        cost_for_call = (d // 60 + 1) * 15
        total_cost += cost_for_call
    return total_cost

N = int(input())
inputs = list(map(int, input().split()))

Y = calYS(inputs)
M = calMS(inputs)

if Y == M:
    print(f"Y M {Y}") # f-string으로 깔끔하게 포매팅
elif Y < M:
    print(f"Y {Y}")
else: # M < Y
    print(f"M {M}")