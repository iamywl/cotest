# src = https://www.acmicpc.net/problem/8958

testcase = int(input())

def sol():
    inputs = []

    res = 0 
    score = 0

    inputs = input()

    for char in inputs:
        if char == 'O':
            score +=1
            res += score
        else:
            score = 0
    return res

for i in range(testcase):
    print(f"{sol()}")
        

    