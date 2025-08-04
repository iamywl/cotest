# Count(list)
T = int(input())
# count : TESTCASE
TESTCASE = 10
adders = 0

def ans(arg):
    prefix_sum = 0
    for j in range(0, T-1):
        # index == max 
        if j == (T-1):
            left_max = max(arg[j-1],arg[j-2])
            righ_max = 0
        # index == max -1
        elif j == (T-2):
            left_max = max(arg[j-1],arg[j-2])
            righ_max = (arg[j+1])
        # index == min index == 0 
        elif j == 0:
            left_max = 0
            righ_max = max(arg[j+1], arg[j+2])
        # index == 1 
        elif j == 1:
            left_max = arg[0]
            righ_max = max(arg[j+1], arg[j+2])
        else: 
            left_max = max(arg[j-1],arg[j-2])
            righ_max = max(arg[j+1], arg[j+2])
            
        max_num = max(left_max, righ_max)

        print(f"j = {j}")
        if ( arg[j] > max_num ):
            adders = arg[j] - max_num
            # print(f"adders = {adders}")
            prefix_sum = prefix_sum + adders

    return prefix_sum

for i in range(1, TESTCASE+1):
    #count 
    inputs = list(map(int, input().split()))
    print(f"#{i} {ans(inputs)}")