# src = https://www.acmicpc.net/problem/2851

testcase = 10


res = 0
inputs = []

# for i in range(10):
#     inputs.append(int(input()))
#     res = res + inputs[i]
#     if res > 100:
#         print(res)

curr = 0

for i in range(10):
    inputs.append(int(input()))
    curr += inputs[i]
    if curr > 100:
        if abs(100 - curr) <= abs(100 - (curr  - inputs[i])):
            print(curr)

        else:
            print(curr-inputs[i])
        break
else:
    print(curr)