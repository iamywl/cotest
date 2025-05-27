#윷 0 
#도 3 
#개 2 
#걸 3 
#모 4 

import sys
input = sys.stdin.readline

def prefixsum(arr):
    temp = 0
    for i in range(len(arr)):
        temp += int(arr[i])
    return temp

for _ in range(3):
    yood = list(map(int, input().split()))
    cnt = prefixsum(yood)

    #도
    if (prefixsum(yood) == 3):
        print("A")
    #개
    if (prefixsum(yood) == 2):
        print("B")
    #걸
    if (prefixsum(yood) == 1):
        print('C')
    #윷
    if (prefixsum(yood) == 0):
        print('D')
    #모
    if (prefixsum(yood) == 4):
        print('E')
    
