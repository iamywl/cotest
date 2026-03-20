A, B = map(int, input().split())

inputs_A = set()
inputs_B = set()

res = []

for ele in range(A):
    inputs_A.add(input())

for ele in range(B):
    inputs_B.add(input())

res = list(inputs_A&inputs_B)

res.sort()
print(len(res))
for ele in res:
    print(ele)
