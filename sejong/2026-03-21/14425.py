N, M = map(int, input().split())
inputs_n =[]
inputs_m =[]
for _ in range(N):
    inputs_n.append(input())

for _ in range(M):
    inputs_m.append(input())

cnt =0
for ele in inputs_m:
    if ele in inputs_n:
        cnt +=1
print(cnt)