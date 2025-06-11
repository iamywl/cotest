# src = https://www.acmicpc.net/problem/2961

N = int(input())
inputs = []
#  input =  ix [Si Bi]
for _ in range(N):
    s, b = map(int, input().split())
    inputs.append([s, b])
# init ax

# min_diff = 10**9 
min_diff = float('inf') 

def make_diff(arg1, arg2):
    if (arg1 - arg2) > 0:
        return (arg1 - arg2)
    elif (arg1 - arg2) < 0:
        return -1 *(arg1 - arg2)
    else: 
        return 0

def solve(idx, CS, CB, stat):
    global min_diff 
    if idx == N:
        if stat > 0:
            diff = make_diff(CS, CB) 
            if diff < min_diff:
                min_diff = diff
        return 
    solve(idx + 1, CS * inputs[idx][0],
          CB + inputs[idx][1], stat + 1)
    solve(idx + 1, CS, CB, stat)
solve(0, 1, 0, 0)
print(min_diff)
